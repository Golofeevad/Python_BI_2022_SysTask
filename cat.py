#!/usr/bin/env python3

import argparse
import os.path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args()

    for file in paths:
        if not os.path.exists(file):
            parser.error('{} does not exist'.format(file))

    for file in paths:
        with open(file) as f:
            for line in f:
                print(line.strip())
        
