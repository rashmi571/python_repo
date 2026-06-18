from unittest import case

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

result=input("enter your choice (+,-,*,/,% ): ")

match result:
    case "+":
        print("sum of two number: ",num1+num2)
    case "-":
        print("difference of two number: ",num1-num2)
    case "*":
        print("multiplication of two number: ",num1*num2)
    case "/":
        print("division of two number: ",num1/num2)
    case "%":
        print("reminder of two number: ",num1%num2)
    case _:
        print("invalid choice")


