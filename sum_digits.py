nums = 123

digit_sum = 0
while nums > 0:
    rem = nums % 10
    digit_sum += rem
    nums //= 10



print("sum of digits : ",digit_sum)