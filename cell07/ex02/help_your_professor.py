#!/bin/python3
def average(class_3):
    total_student = len(class_3)
    total_score = 0
    for score in class_3.values():
        total_score += score
    return total_score/total_student


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")