#!/bin/python3
import sys

def downcase_it(string_argu):
    return string_argu.lower()

para_len = len(sys.argv)
if  para_len < 2:
    print("none")
else:
    for i in range(1, para_len):
        print(downcase_it(sys.argv[i]))