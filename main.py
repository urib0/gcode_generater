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

arg = parser()

# ファイルの存在チェック
input_file_name = arg.filename if arg.filename else "input.txt"
input_file_path = os.path.join(os.getcwd(), input_file_name)
output_file_name = arg.another_file if arg.another_file else "output.txt"
output_file_path = os.path.join(os.getcwd(), output_file_name)

if not os.path.isfile(input_file_path):
    print(f"file does not exist:{input_file_name}")
    exit(0)

# 入力ファイル読み込み
with open(input_file_path,"r") as f:
    lines = f.readlines()

for line in lines:
	if not line[0] in ["#","\n"]:
		print(line.split(","))
