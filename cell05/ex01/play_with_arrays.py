#!/bin/python3
org_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for a in org_array:
    a += 2
    new_array.append(a)

print("Original array:",org_array)
print("New array:",new_array)