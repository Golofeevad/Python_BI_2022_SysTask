#!/usr/bin/env python3

import sys
import os
import argparse


def bytes_count(path):
    return os.path.getsize(path)


def lines_count(file):
    return len(file.readlines())


def word_count(file):
    return len(file.read().split())


def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f'readable_file:{path} is not a valid path')


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--bytes', action='store_true')
parser.add_argument('-l', '--lines', action='store_true')
parser.add_argument('-w', '--words', action='store_true')
parser.add_argument('path', nargs='?', default=sys.stdin)
args = parser.parse_args()

def main(*args):
    for arg in args:
        path_to_file = file_path(arg.path)
        if arg.bytes:
            print(bytes_count(path_to_file))
        with open(path_to_file) as f:
            if arg.lines:
                print(lines_count(f))
            if arg.words:
                print(word_count(f))


if __name__ == '__main__':
    main(args)
