#!/bin/bash
# Version: 1.0
# Date: 2021-10-20
# This bash script generates Open-CMSIS-Pack Documentation:
#
# Pre-requisites:
# - bash shell (for Windows: install git for Windows)
# - doxygen 1.9.2

set -o pipefail

DIRNAME=$(dirname $(readlink -f $0))
DOXYGEN=$(which doxygen)

if [[ ! -f "${DOXYGEN}" ]]; then
    echo "Doxygen not found!" >&2
    echo "Did you miss to add it to PATH?"
    exit 1
else
    version=$("${DOXYGEN}" --version | sed -r -e 's/.*([1-9][0-9]*\.[0-9]+\.[0-9]+).*/\1/')
    echo "DOXYGEN is ${DOXYGEN} at version ${version}"
    if [[ "${version}" != "1.9.2" ]]; then
        echo " >> Version is different from 1.9.2 !" >&2
    fi
fi

function doxygen {
    pushd "$(dirname $1)" > /dev/null
    echo "${DOXYGEN} $1"
    "${DOXYGEN}" $(basename "$1")
    popd > /dev/null

    if [[ $2 != 0 ]]; then
        cp -f "${DIRNAME}/templates/search.css" "${DIRNAME}/../doc/html/search/"
    fi

    projectName=$(grep -E "PROJECT_NAME\s+=" $1 | sed -r -e 's/[^"]*"([^"]+)"/\1/')
    projectNumber=$(grep -E "PROJECT_NUMBER\s+=" $1 | sed -r -e 's/[^"]*"([^"]+)"/\1/')
    datetime=$(date -u +'%a %b %e %Y %H:%M:%S')
    sed -e "s/{datetime}/${datetime}/" "${DIRNAME}/templates/cmsis_footer.js" \
        | sed -e "s/{projectName}/${projectName}/" \
        | sed -e "s/{projectNumber}/${projectNumber}/" \
        > "${DIRNAME}/../doc/${partname}/html/cmsis_footer.js"
}

echo "Cleaning existing documentation ..."
find "${DIRNAME}/../doc/" -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

echo "Generating documentation ..."
doxygen "${DIRNAME}/pack.dxy" 1

exit 0
