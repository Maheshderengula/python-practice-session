rows=4
for i in range(rows,0,-1):
    for j in range(68,68 - i,-1): #ascii 68 ='D'
        print(chr(j),end=" ")
    print()    