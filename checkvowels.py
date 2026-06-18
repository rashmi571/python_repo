char=input("enter the char: ")

match char:
    case "a" | "e" | "i" | "o" | "u":
        print("vowel")
    case _:
        print("consonant")