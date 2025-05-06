#!/bin/python3
import sys

def shrink(para_string):
    print(para_string[slice(8)])

def enlarge(para_string):
    while len(para_string) < 8:
        para_string += "Z"
    print(para_string)

para_len = len(sys.argv)
if(para_len < 2):
    print("none")
else:
    for i in range(1, para_len):
        temp_str = sys.argv[i]
        if len(temp_str) == 8:
            print(temp_str)
        elif len(temp_str) < 8:
            enlarge(temp_str)
        else:
            shrink(temp_str)