s="I love programming"
long_word=""
word=""
for char in s:
    if char!=" ":
        word+=char 
    else:
        if len(word)>len(long_word):
            long_word=word 
        word=""

if len(word)>len(long_word):
    long_word=word 
    
print(long_word)

#
s="I love programming"
long_word=""
word=""
i=0 
while i<len(s):
    if s[i]!=" ":
        word+=s[i]
    else:
        if len(word)>len(long_word):
            long_word=word 
        word="" 
    i+=1
    
if len(word)>len(long_word):
    long_word=word 
print(long_word)

# 
s="I love programming".split()
long_word=""
for word in s:
    if len(word)>len(long_word):
        long_word=word 
print(long_word)
        
        
        

