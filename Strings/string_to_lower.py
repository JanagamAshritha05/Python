s="HELLO"  
print(s.lower())

# 
s="HELLO"
new=""
for char in s:
    new+=char.lower()
print(new)

# 
s="HELLO"
new=""
i=0 
while i<len(s):
    new+=s[i].lower() 
    i+=1 
print(new)

# 
s="HELLO"
new=""
for char in s:
    if "A"<=char<="Z":
        new+=chr(ord(char)+32) 
    else:
        new+=char 
print(new)

#
s="HELLO"
new=""
for char in s:
    if ord("A")<=ord(char)<=ord("Z"):
        new+=chr(ord(char)+32) 
    else:
        new+=char 
print(new)



