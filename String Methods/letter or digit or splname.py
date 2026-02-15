n=input()
if n.isdigit():
    print("Digit")
elif n.isupper():
    print("Uppercase Letter")
elif n.islower():
    print("Lowercase Letter")
else:
    print("Special Character")
    