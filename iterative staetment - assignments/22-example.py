num = 153 
sum_val =0
temp = num
while temp> 0:
    digit = temp %10
    sum_val +=digit **3
    temp //=10

if sum_val == num:
    print(num,"is an armstrong number")

else:
    print(num,"is not an armstrong number")