n=input("enter the day  number: ")

match n:
    case 1 | 2 | 3 | 4 | 5:
        print("week days")
    case 6 | 7 :
        print("weekend days")
    case _ :
        print("day not exist")