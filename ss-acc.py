#!/usr/bin/env python3

import re
import numpy as np
import argparse

CLI = argparse.ArgumentParser()

CLI.add_argument(
    '-i',
    '--filename',
    nargs="?",
    type=str,
    default=None,
    help='input file path'
)

ARGS = CLI.parse_args()

A = ARGS.filename

def parseDSSP(file):
    dat = open(file,'r')

    aa = []
    acc = []

    line_num = 0
    start = False
    for line in dat:
        if (re.search('#',line)):
            start=True
            continue
        if(start):
            aa.append(line[12:14].strip())
            acc.append(line[34:38].strip())
    merged_list = tuple(zip(aa,acc))

    return merged_list

def ssACC(file):

    input = parseDSSP(file)

    sslist = []

    for i in range(0,len(input)):
        if input[i][0].islower():
            sslist.append(input[i][1])
    array = np.array(sslist).astype(np.float)

    if len(array)>=1:
        print(np.mean(array))
    else:
        print('NA')
    
ssACC(A)