#!/usr/bin/env python3

import os
import argparse


def find_files(path):
    return os.listdir(path)


parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='*', default=[os.getcwd()])
parser.add_argument('-a', '--all', action='store_true')
args = parser.parse_args()


def main(*args):
    for arg in args:
        if os.path.exists(arg):
            files = find_files(path=arg)
            if parser.parse_args().all:
                print(*sorted(files))
            else:
                print(*sorted(filter(lambda x: not x.startswith('.'), files)))
        else:
            print(f'{arg} is not a directory')


if __name__ == '__main__':
    main(*args.path)
