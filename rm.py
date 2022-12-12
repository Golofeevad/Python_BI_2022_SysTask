#!/usr/bin/env python3

import argparse
import os
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '-R', '--recursive', action='store_true')
    parser.add_argument('path', nargs='*')
    args = parser.parse_args()

    path = args.path
    if args.recursive:
        for path in args.path:
            shutil.rmtree(path)
    else:
        for path in args.path:
            if os.path.isdir(path):
                parser.error('{}: is a directory'.format(path))
            else:
                os.remove(path)
