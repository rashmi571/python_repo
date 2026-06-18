s = input("enter string to check palindrome:  ").lower()

copy_s = s

rev = s[::-1]

if copy_s == rev:
    print("This is palindrome string")
else:
    print("This is not palindrome string")