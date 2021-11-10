#!/usr/bin/python3

import os
import shutil

from argparse import ArgumentParser
from multiprocessing.pool import ThreadPool
from pathlib import Path
from progress.bar import Bar
from urllib.request import urlretrieve
from urllib.parse import urlparse, urljoin
from xml.dom import minidom

KEIL_INDEX = 'https://www.keil.com/pack/index.pidx'
OUTPUT = '.Web'

def fetch_pdsc(item, output, cache_url):
    pdsc_filename = f"{item.attributes['vendor'].value}.{item.attributes['name'].value}.pdsc"
    pdsc_file = output.joinpath(pdsc_filename)

    if not pdsc_file.exists():
        try:
            urlretrieve(urljoin(cache_url, pdsc_filename), pdsc_file)
        except Exception:
            try:
                urlretrieve(urljoin(item.attributes['url'].value, pdsc_filename), output.joinpath(pdsc_file))
            except Exception:
                pass

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--index', type=urlparse, default=KEIL_INDEX, help='The pack index to download.')
    parser.add_argument('-p', '--pdsc', type=urlparse, help='Base URL for cached pdsc files in index. Defaults to basename of index file.')
    parser.add_argument('-o', '--output', type=Path, default=OUTPUT, help='Output folder')
    parser.add_argument('-j', '--threads', type=int, default=8, help='Number of parallel downloads')
    parser.add_argument('-f', '--force', action='store_true', help='Force download')
    args = parser.parse_args()

    index_filename = Path(args.index.path).name
    index_file = args.output.joinpath(index_filename)
    cache_url = args.pdsc
    if not cache_url:
        cache_url = urljoin(args.index.geturl(), '.')

    if args.force:
        try:
            shutil.rmtree(args.output)
        except OSError as e:
            pass

    try:
        os.makedirs(args.output)
    except OSError:
        pass

    print(f"Downloading {args.index.geturl()} ...")
    urlretrieve(args.index.geturl(), index_file)

    print(f"Parsing {index_file} ...")
    indexXML = minidom.parse(str(index_file))

    pdscs = indexXML.getElementsByTagName('pdsc')

    print('Downloading pdsc files ...')
    with ThreadPool(args.threads) as pool:
        bar = Bar('Processing', max=len(pdscs))
        for i in pool.imap_unordered(lambda pdsc: fetch_pdsc(pdsc, args.output, cache_url), pdscs):
            bar.next()
        bar.finish()

if __name__ == "__main__":
    main()
