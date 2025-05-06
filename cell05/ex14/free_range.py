#!/bin/python3
import sys

if len(sys.argv) < 2 + 1:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = []

    for value in range(start, end+1):
        result.append(value)
    print(result)
    