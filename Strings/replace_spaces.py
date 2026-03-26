#Replace Spaces with Hyphen

s="hello world"
new=""
for char in s:
    if char==" ":
        new+="-"
    else:
        new+=char 
print(new)

#
s="hello world"
print(s.replace(" ", "-"))

# 
s = "hello world"
new = ""
for i in range(len(s)):
    if s[i] == " ":
        new += "-"
    else:
        new += s[i]
print(new)






