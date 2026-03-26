
s="I love programming".split() 
new=[]
for word in s:
    new.append(len(word)) 
new.sort(reverse=True)
print(new[0])

# 
s="I love programming"
max_len=0 
word=""
for char in s:
    if char!=" ":
        word+=char 
    else:
        if len(word)>max_len:
            max_len=len(word)
        word=""

if len(word)>max_len:
    max_len=len(word) 
print(max_len)

# 
s="I love programming"
max_len=0 
count=0 
for i in range(len(s)):
    if s[i]!=" ":
        count+=1 
    else:
        if count>max_len:
            max_len=count 
        count=0 
        
if count>max_len:
    max_len=count 
print(max_len)

        
        
        
        
 