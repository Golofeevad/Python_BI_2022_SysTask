#!/usr/bin/env python3

import argparse
import os.path
import sys
from collections import deque

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', nargs='?', type=int, default=10)
    parser.add_argument('file', nargs='?')
    parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    (args, _) = parser.parse_known_args()
    file_path = args.file
    if file_path is None:
        if not sys.stdin.isatty():
            content = parser.parse_args().stdin.read().splitlines()
        else:
            content = []
        content_len = len(content)
        for i in range(max(0, content_len - args.n), content_len):
            print(content[i])
    else:
        q = deque(maxlen=args.n)
        if not os.path.exists(file_path):
            parser.error('{} does not exist'.format(file_path))
        with open(file_path) as file:
            for line in file:
                q.append(line)

        for line in q:
            print(line, end="")
