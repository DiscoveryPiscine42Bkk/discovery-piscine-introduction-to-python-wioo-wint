import sys

para_len = len(sys.argv)

if para_len < 2:
    print("none")
else:
    for i in range(para_len):
        if(i+1 < para_len): #prevent index of range
            if sys.argv[i+1].endswith("ism") is False:
                print(sys.argv[i+1]+"ism")