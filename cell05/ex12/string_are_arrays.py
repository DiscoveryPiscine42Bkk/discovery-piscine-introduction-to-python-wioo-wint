#!/bin/python3
import sys

para_len = len(sys.argv)

if para_len < 2:
    print("none")
else:
    output = ""
    for z in sys.argv[1]:
        if z == "z":
            output += z
    if output == "": #sys.argv[1].find("z")
        print("none")
    else:
        print(output)