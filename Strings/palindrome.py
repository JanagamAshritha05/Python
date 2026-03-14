s="Madam".lower() 
new=""
for char in s:
    new=char+new 

if new==s:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 
s="Madam".lower()
res=s[::-1]
if s==res:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 
s = "Madam"
s = s.lower()
print("Palindrome" if s == s[::-1] else "Not a Palindrome")

