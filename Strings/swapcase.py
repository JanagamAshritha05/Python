
s='AbC'
new=""
for char in s:
    if char.islower():
        new+=char.upper() 
    else:
        new+=char.lower() 
print(new)

# 
s="AbC" 
print(s.swapcase())

# 
s="AbC"
new=""
for char in s:
    if "a"<=char<="z":
        new+=chr(ord(char)-32)
    elif "A"<=char<="Z":
        new+=chr(ord(char)+32)
    else:
        new+=char 
print(new)
        
        
        


