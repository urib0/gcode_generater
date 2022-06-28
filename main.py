#!/usr/bin/env python3

import sys
import os
from argparse import ArgumentParser

def parser():
    usage = 'Usage: ./main.py input.txt [-o <file>] [--help]'\
            .format(__file__)
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('filename', type=str,
                           help='input file name')
    argparser.add_argument('-o', type=str,
                           dest='another_file',
                           help='ouput file name')
    args = argparser.parse_args()
    return args

print(parser())
