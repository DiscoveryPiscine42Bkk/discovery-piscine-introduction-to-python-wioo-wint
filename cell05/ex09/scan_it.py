#!/bin/python3
import sys
import re

if len(sys.argv) < 2 + 1:
    print("none")
else:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]

    search = re.findall(keyword, string_to_search)
    print(len(search))
    