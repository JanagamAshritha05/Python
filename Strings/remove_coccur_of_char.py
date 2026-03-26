

s="banana"
c="a" 
new=""
for char in s:
    if char==c:
        continue 
    else:
        new+=char
print(new)

#
s="banana"
c="a" 
new=""
for char in s:
    if char != c:
        new += char
print(new)

# 
s="banana"
c="a"
new=""
i=0 
while i<len(s):
    if s[i]!=c:
        new+=s[i]
    i+=1 
print(new)



