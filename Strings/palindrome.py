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

# 

def is_palindrome(s):
    temp = ""
    for char in s:
        if "A" <= char <= "Z":
            temp += chr(ord(char) + 32) 
        else:
            temp += char 
        
    rev = ""

    for i in range(len(temp)-1, -1, -1):
        rev += temp[i] 

    if temp == rev:
        res = "palindrome"
    else:
        res = "not Palindrome"
    
    return res 


s = "Madam"
res = is_palindrome(s)
print(res)








