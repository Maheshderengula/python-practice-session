num = int (input("enter a single digit number (0-9):"))
digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]

if 0 <= num <=9:
    print("in english:",digits[num])

else:
    print("not a single digit number")
    