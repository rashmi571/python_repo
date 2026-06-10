nums = 123

rev=0

while nums > 0:
    digits = nums%10
    rev = (rev * 10) + digits
    nums //= 10

print("Reversed Numbers is: ",rev)