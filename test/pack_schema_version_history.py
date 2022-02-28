#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import subprocess
import sys
from pathlib import Path

from dateutil.parser import parse

DIRNAME = Path(__file__).parent
PATTERN = "::error file={},line={}::{}"

rc = 0


def log_error(file, line, message):
    global rc
    print(PATTERN.format(file.relative_to(DIRNAME.joinpath("..")), line, message))
    rc = 1


def get_from_cmd(cmd, cwd=Path.cwd()):
    print("./"+cwd.relative_to(Path.cwd()).as_posix(), "$", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, cwd=cwd)
    stdout = result.stdout.decode("utf-8").strip()
    stderr = result.stderr.decode("utf-8").strip()
    if stdout:
        print(">", stdout)
    if stderr:
        print(">", stderr)
    print()
    return stdout


def main():
    print("Checking PACK.xsd version information...\n")

    schema_file = DIRNAME.joinpath('../schema/PACK.xsd')
    dxy_file = DIRNAME.joinpath('../doxygen/pack.dxy')
    doc_file = DIRNAME.joinpath('../doxygen/src/General.txt')

    date_pattern = re.compile('\\$Date:\\s+(\\d+\\. \\w+ \\d{4})')
    rev_pattern = re.compile('\\$Revision:\\s+(\\d+\\.\\d+\\.\\d+)')
    version_pattern = re.compile('SchemaVersion=(\\d+\\.\\d+\\.\\d+)')
    history_pattern = re.compile('(\\d+\\. \\w+ \\d{4}): v(\\d+\\.\\d+\\.\\d+)')
    property_pattern = re.compile('^\\s*<xs:schema.*version="([^"]+)".*>\\s*$')

    date = (None, 0)
    revision = (None, 0)
    version = (None, 0)
    history = (None, 0)
    xsproperty = (None, 0)

    with(open(schema_file)) as schema:
        for i, line in enumerate(schema):
            date = (date_pattern.search(line), i) if not date[0] else date
            revision = (rev_pattern.search(line), i) if not revision[0] else revision
            version = (version_pattern.search(line), i) if not version[0] else version
            history = (history_pattern.search(line), i) if not history[0] else history
            xsproperty = (property_pattern.search(line), i) if not xsproperty[0] else xsproperty

    date = (parse(date[0][1]), date[1] + 1) if date[0] else None
    revision = (revision[0][1], revision[1] + 1) if revision[0] else None
    version = (version[0][1], version[1] + 1) if version[0] else None
    history = (parse(history[0][1]), history[0][2], history[1] + 1) if history[0] else None
    xsproperty = (xsproperty[0][1], xsproperty[1] + 1) if xsproperty[0] else None

    author_date = parse(get_from_cmd(['git', 'log', '-1', '--pretty=%ad', '--date=format:%Y-%m-%d', schema_file.name],
                                     cwd=schema_file.parent))
    base_rev = get_from_cmd(['git', 'log', '-1', '--pretty=%P', schema_file.name], cwd=schema_file.parent)
    head_rev = get_from_cmd(["git", "log", "-1", '--pretty=%H', schema_file.name], cwd=schema_file.parent)
    blame = get_from_cmd(["git", "blame", f"{base_rev}..{head_rev}", "-l", "-L", f"{revision[1]},{revision[1]}",
                          schema_file.name], cwd=schema_file.parent)
    blamed_rev = blame.split(' ')[0]

    dxy_version_pattern = re.compile('PROJECT_NUMBER\s*=\s*"Version (\\d+\\.\\d+\\.\\d+)"')

    dxy_version = (None, 0)
    with(open(dxy_file)) as dxy:
        for i, line in enumerate(dxy):
            dxy_version = (dxy_version_pattern.search(line), i) if not dxy_version[0] else dxy_version
    dxy_version = (dxy_version[0][1], dxy_version[1] + 1) if dxy_version[0] else None

    history_version_pattern = re.compile('<td>(\\d+\\.\\d+\\.\\d+)</td>')
    history_version = dict()
    with(open(doc_file)) as doc:
        accept = False
        for i, line in enumerate(doc):
            if line == '<table class="cmtable" summary="Revision History">\n':
                accept = True
            if accept:
                if line == '</table>':
                    break
                v = history_version_pattern.search(line)
                if v:
                    history_version[i + 1] = v[1]

    if not date:
        log_error(schema_file, 0, "Modification date tag '$Date:' missing!")
    elif date[0] != author_date:
        log_error(schema_file, date[1], "Modification date tag not updated, "
                                        f"should be {author_date.strftime('%d. %b %Y')}")

    if not revision:
        log_error(schema_file, 0, "Latest version tag '$Revision:' missing!")
    elif head_rev != blamed_rev:
        log_error(schema_file, revision[1], f"Revision tag not updated, should be incremented!")
    else:
        if not version:
            log_error(schema_file, 0, "Schema version tag 'SchemaVersion' missing!")
        elif version[0] != revision[0]:
            log_error(schema_file, version[1], f"Schema version tag not updated, should be {revision[0]}")

        if not history:
            log_error(schema_file, 0, "Change history missing!")
        elif history[1] != revision[0] or history[0] != author_date:
            log_error(schema_file, history[2], "Change history not updated, should contain "
                                               f"{author_date.strftime('%d. %B %Y')}: v{revision[0]}")
        if not xsproperty:
            log_error(schema_file, 0, "xs:schema property 'version' missing!")
        elif xsproperty[0] != revision[0]:
            log_error(schema_file, xsproperty[1], f"xs:schema property 'version' not updated, should be {revision[0]}")

        if not dxy_version:
            log_error(dxy_version, 0, "PROJECT_VERSION missing!")
        elif dxy_version[0] != revision[0]:
            log_error(dxy_file, dxy_version[1], f"PROJECT_VERSION not updated, should be {revision[0]}")

        if revision[0] not in history_version.values():
            line = sorted(history_version.keys())[0]
            log_error(doc_file, line, "Revision History not updated, should contain "
                                      f"table row for version {revision[0]}")


if __name__ == "__main__":
    if 'schema/PACK.xsd' in sys.argv \
            or 'test/pack_schema_version_history.py' in sys.argv:
        main()

    sys.exit(rc)
