a = int (input("enter frist number:"))
b = int (input("enter second number:"))
c = int (input("enter three number:"))

max_num = a if (a>b and a>c) else (b if b>c else c)
print("maximum number is:", max_num)