rows = 5
for i in range(1, rows + 1):
    val = i
    for j in range(1, i + 1):
        print(chr(64 + val), end=" ")
        if j % 2 == 1:
            val = rows - j + 1
        else:
            val = val + i
    print()
