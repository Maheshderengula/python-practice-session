rows = 6
for i in range (1,rows + 1):
    val = i
    for j in range(1,i+1):
        print(val,end=" ")
        val += rows - j
    print()    