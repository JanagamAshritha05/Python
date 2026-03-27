#Remove All Special Characters

s="a@b#c$1"
new=""
for char in s:
    if char.isalnum():
        new+=char 
print(new)

# 
s="a@b#c$1"
new=""
i=0 
while i<len(s):
    if s[i].isalnum():
        new+=s[i] 
    i+=1 
print(new)

#
s="a@b#c$1"
new=""
for char in s:
    if "a"<=char<="z" or "A"<=char<="Z" or "0"<=char<="9":
        new+=char 
print(new)

#
s = "a@b#c$1"
new = ""
for char in s:
    if (ord(char) >= 48 and ord(char) <= 57) or \
       (ord(char) >= 65 and ord(char) <= 90) or \
       (ord(char) >= 97 and ord(char) <= 122):
        new += char
print(new)




