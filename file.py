
age=int(input("enter your age: "))
card=input("enter your pass name: ")

if age >= 18:
    if card == "welcome":
        print("welcome for party")
    elif card == "member":
        print("member of party")
    else:
        print("you are entered in party")
else:
    print("your age is low")