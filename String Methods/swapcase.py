string=input()
print(string.swapcase())

#second answer 
string=input()
new=""
for char in string:
    if char.isupper():
        new+=char.lower()
    else:
        new+=char.upper()
print(new)

