eng=int(input("enter your english marks: "))
hindi=int(input("enter your hindi marks: "))
maths=int(input("enter your maths marks: "))
sci=int(input("enter your science marks: "))
art=int(input("enter your art marks: "))

total = eng + hindi + maths + sci + art

print("\nyour total marks is: ",total)

per=total / 500 * 100

print("your percentage is: ",per)

if per>=75:
    print("\nhonour")
elif 60 <= per < 75:
    print("\nIst division")
elif 45 <= per < 60:
    print("\nIIst division")
elif 33 <= per < 40:
    print("\nIIIst division")
else:
    print("\nfail")


