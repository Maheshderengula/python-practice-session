rows =4
for i in range(1,rows + 1):
    for j in range(65,65 +i): # ASCII 65 ='A'
        print(chr (j),end="")
    print()