x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
result = x * y

print(x , " x " , y , " = " , result)

if result < 0:
    print("This number is negative.")
elif result == 0:
    print("This number is positive and negative.")
else:
    print("This number is positive.")