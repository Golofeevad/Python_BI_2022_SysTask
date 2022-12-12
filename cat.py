#!/usr/bin/env python3

import argparse
import os.path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    path = args.path
    if not os.path.exists(path):
        parser.error('{} does not exist'.format(path))

    with open(args.path) as file:
        print(file.read())
