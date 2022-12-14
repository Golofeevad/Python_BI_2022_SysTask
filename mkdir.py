#!/usr/bin/env python3

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-p', action='store_true')
    args = parser.parse_args()

    path = args.path
    if args.p:
        os.makedirs(path)
    else:
        try:
            os.mkdir(path)
        except FileNotFoundError as e:
            parser.error('{} does not exist'.format(e.filename))
