#!/usr/bin/env python3

import argparse
import os.path
import pathlib
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '-R', '--recursive', action='store_true')
    parser.add_argument('from_dir')
    parser.add_argument('to_dir')
    args = parser.parse_args()

    from_dir = pathlib.Path(args.from_dir)
    to_dir = pathlib.Path(args.to_dir)
    if args.recursive:
        shutil.copytree(from_dir, to_dir.joinpath(from_dir.name))
    else:
        try:
            if os.path.isdir(to_dir):
                shutil.copyfile(from_dir, to_dir.joinpath(from_dir.name))
            else:
                shutil.copyfile(from_dir, to_dir)
        except IsADirectoryError as e:
            parser.error("Is a directory: {}".format(e.filename))
        except FileNotFoundError as e:
            parser.error("{} does not exist".format(e.filename))
