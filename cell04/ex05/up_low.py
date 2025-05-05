input_string = input("Enter a string: ")
result = ""
for s in input_string:
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()

print(result)