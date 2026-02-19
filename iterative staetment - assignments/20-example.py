import sys

numbers = sys.argv[1:6]  # first 5 arguments
for n in numbers:
    n = int(n)
    if n % 2 == 0:
        print(n)
