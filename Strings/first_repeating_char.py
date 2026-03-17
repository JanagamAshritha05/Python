
s="aabbcde"

for char in s:
    count=s.count(char)
    if count>1:
        print(char)
        break 
    
# 
s="aabbcde"
freq={}
for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 
        
for char, count in freq.items():
    if count>1:
        print(char)
        break 
    

# 
s="aabbcde"
freq={}
i=0 
while i<len(s):
    if s[i] in freq:
        freq[s[i]]+=1 
    else:
        freq[s[i]]=1 
    i+=1 
    
for char, count in freq.items():
    if count>1:
        print(char)
        break 
    


