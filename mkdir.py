#!/usr/bin/env python3

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-p', action='store_true')
    args = parser.parse_args()

    path = args.path
    if args.p:
        os.makedirs(path)
    else:
        os.mkdir(path)
