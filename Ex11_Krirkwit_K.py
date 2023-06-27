number = int(input("enter number"))
for i in range(number):
    print(" "*(number-(i+1)) + "*"*((i+1)+(i*1)))