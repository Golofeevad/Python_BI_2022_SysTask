#!/usr/bin/env python3

import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '-R', '--recursive', action='store_true')
    parser.add_argument('from_dir')
    parser.add_argument('to_dir')
    args = parser.parse_args()

    from_dir = args.from_dir
    if args.recursive:
        shutil.copytree(from_dir, args.to_dir)
    else:
        try:
            shutil.copyfile(from_dir, args.to_dir)
        except IsADirectoryError:
            parser.error("Is a directory: {}".format(from_dir))
        except FileNotFoundError as e:
            parser.error("{} does not exist".format(e.filename))
