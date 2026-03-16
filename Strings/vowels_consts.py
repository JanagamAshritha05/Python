
s="programming" 
v=0
c=0 
for char in s:
    if char in "aeiouAEIOU":
        v+=1 
    else:
        c+=1 

print("Vowels:", v)
print("consonants:", c) 

# 
s="programming" 
v=0 
c=0 
i=0 
while i<len(s):
    if s[i] in "aeiouAEIOU":
        v+=1 
    else:
        c+=1 
    i+=1 

print("Vowels:", v)
print("consonants", c) 

# 
s="programming".lower()
v=sum(1 for char in s if char in "aeiou")
c=len(s)-v 

print("vowels:", v)
print("consonants:", c)


