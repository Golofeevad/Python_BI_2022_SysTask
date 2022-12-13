#!/usr/bin/env python3

import os
import argparse
import sys


class PathDoesntExist(ModuleNotFoundError):
    pass


parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
args = parser.parse_args()


if __name__ == '__main__':
    text = []
    if not args.path:
        file = sys.stdin.read()
        for line in file:
            text.append(line)

    else:
        if os.path.exists(args.path):
            with open(args.path, 'r') as f:
                for line in f:
                    text.append(line.rstrip('\n'))
        else:
            raise PathDoesntExist

    text.sort()

    for line in text:
        print(line, end='\n')
