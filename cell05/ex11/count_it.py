#!/bin/python3
import sys

para_len = len(sys.argv)

if  para_len < 2:
    print("none")
else:
    print("parameters:", para_len - 1)
    for i in range(para_len):
        if(i+1 < para_len): #prevent index of range
            parameter = sys.argv[i+1]
            print(parameter,":", len(parameter))