#!/usr/bin/env python3

import argparse
import os.path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    file_path = args.path
    if not os.path.exists(file_path):
        parser.error('{} does not exist'.format(file_path))

    previous_line = None
    with open(file_path) as file:
        for line in file:
            if previous_line != line:
                print(line, end="")
                previous_line = line
