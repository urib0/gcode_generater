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

def g2dict(input_):
    #* inputをコマンドと引数のリストに分け，リストにする
    splited_input = input_.split(' ')
    codeName = splited_input[:1]
    param_E = [splited_input[i][1:] for i in range(1, len(splited_input))]
    param_S = [splited_input[i][:1].upper() for i in range(1, len(splited_input))]
    param = {param_S[i]:param_E[i] for i in range(0, len(splited_input)-1)}

    #* 作ったリストをソートし，元の体裁で返す
    param = sorted(param.items())
    locations = [param[i][0] for i in range(0, len(param))]
    values = [float(param[i][1])for i in range(0, len(param))]
    newParam = dict(zip(locations, values))
    return newParam

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

target = {
    "X": 0,
    "Y": 0,
    "Z": 0,
    "R": 0,
    "P": 0
}

for line in lines:
	if not line[0] in ["#","\n"]:
		step = int(line.split(",")[0])
		gstart = g2dict(line.split(",")[1])
		gend = g2dict(line.split(",")[2])
		for i in range(step+1):
			for pos in gstart.keys():
				diff = i*(gend[pos]-gstart[pos])/step
				target[pos] = gstart[pos]+diff
			gcode = f'G1 X{target["X"]} Y{target["Y"]} Z{target["Z"]} R{target["R"]} P{target["P"]}'
			print(gcode)






