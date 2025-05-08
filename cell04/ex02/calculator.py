#!/bin/python3
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")
print(num1, " + ", num2, " = ", num1+num2)
print(num1, " - ", num2, " = ", num1-num2)
if num2 == 0:
    print("Error! Can't be divided by Zero")
else:
    print(num1, " / ", num2, " = ", num1/num2)
print(num1, " * ", num2, " = ", num1*num2)