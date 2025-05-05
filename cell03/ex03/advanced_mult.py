x = 0
y = 0
result = ""

while x < 11:
    while y < 11:
        result += str(x * y) + " "
        y += 1
    print ("Table de ",x,":", result)
    result = ""
    y = 0
    x += 1