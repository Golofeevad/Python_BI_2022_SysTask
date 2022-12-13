#!/usr/bin/env python3

import sys
import os
import argparse


def bytes_count(file):
    return sys.getsizeof(file) - sys.getsizeof('')


def lines_count(file):
    return file.count('\n')


def word_count(file):
    return len(file.split())


def file_path(path):
    if os.path.exists(path.name):
        return path
    else:
        raise argparse.ArgumentTypeError(f'{path} is not a valid path')


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--bytes', action='store_true')
parser.add_argument('-l', '--lines', action='store_true')
parser.add_argument('-w', '--words', action='store_true')
parser.add_argument('path', nargs='?', default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()


functions = {'lines': lines_count, 'words': word_count, 'bytes': bytes_count}


def only_path(args):
    del args['path']
    if any(args.values()):
        return [arg for arg, req in args.items() if req]
    else:
        return list(args.keys())


if __name__ == '__main__':
    if file_path(args.path):
        file = args.path.read()
        arguments = only_path(vars(args))
        count = []
        for arg in arguments:
            count.append(functions[arg](file))
        print(' '.join(map(str, count)))
