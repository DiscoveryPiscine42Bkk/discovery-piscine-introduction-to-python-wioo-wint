#!/bin/python3
import sys

para_len = len(sys.argv)

if  para_len < 2 + 1:
    print("none")
else:
    for para in sys.argv:
        if para_len > 1:
            print(sys.argv[para_len-1])
            para_len -= 1