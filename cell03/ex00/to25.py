input_num = int(input("Enter a number less than 25:"))

if input_num > 25:
    print("Error")
else:
    for n in range(input_num, 26):
        print("Inside the loop, my variable is ", n)