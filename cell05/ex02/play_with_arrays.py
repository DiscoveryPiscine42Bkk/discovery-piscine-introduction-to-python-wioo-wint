#!/bin/python3
org_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for a in org_array:
    if a > 5:
        a += 2
        new_array.append(a)

print(org_array)
print(new_array)