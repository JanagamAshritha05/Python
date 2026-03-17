
s="hello"
new=""
for char in s:
    new+=char.upper() 
print(new)

#
print(s.upper())

# 
s = "hello"
new = ""
i = 0
while i < len(s):
    new += s[i].upper()
    i += 1
print(new)

#
s="hello"
new=""
for char in s:
    if "a"<=char<="z":
        new+=chr(ord(char)-32) 
    else:
        new+=char 
print(new)        
        
# 
s="hello"
new=""
for char in s:
    if 97<=ord(char)<=122:
        new+=chr(ord(char)-32) 
    else:
        new+=char 
print(new)        
        
        

"""
ord('a') = 97
ord('A') = 65
# difference = 32

# so lowercase - 32 = uppercase
ord('h') = 104
104 - 32 = 72
chr(72) = 'H' 

ASCII values:
a = 97    A = 65
b = 98    B = 66
c = 99    C = 67
...
z = 122   Z = 90

Difference = 32

So → lowercase - 32 = uppercase

"""

