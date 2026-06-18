a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))

if b <= a >= c:
    print("a is maximum number.")
elif a <= b >= c:
    print("b is maximum number.")
else:
    print("c is maximum number.")