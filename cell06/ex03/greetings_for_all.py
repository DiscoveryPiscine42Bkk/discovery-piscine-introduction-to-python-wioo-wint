#!/bin/python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print("Hello, "+name+".")
    else:
        print("Error! It was not a name.")

greetings('Wint')
greetings('Winoo')
greetings()
greetings(42)