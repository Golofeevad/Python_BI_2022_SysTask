#!/usr/bin/env python3

import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('from_dir')
    parser.add_argument('to_dir')
    args = parser.parse_args()

    from_dir = args.from_dir
    try:
        shutil.move(from_dir, args.to_dir)
    except FileNotFoundError as e:
        parser.error('{} does not exist'.format(e.filename))
