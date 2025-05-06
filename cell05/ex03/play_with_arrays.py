#!/bin/python3
org_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for a in org_array:
    if a > 5:
        a += 2
        new_set.add(a)

print(org_array)
print(new_set)