#!/usr/bin/env python3

import argparse
import re
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern')
    parser.add_argument('file', nargs='?')
    parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    (args, _) = parser.parse_known_args()

    pattern = re.compile(args.pattern)
    if args.file is None:
        if not sys.stdin.isatty():
            content = parser.parse_args().stdin.read().splitlines()
        else:
            content = []
        for line in content:
            if pattern.search(line) is not None:
                print(line)
    else:
        with open(args.file) as file:
            for line in file:
                if pattern.search(line) is not None:
                    print(line, end="")
