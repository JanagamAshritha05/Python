
s="banana"

for char in set(s):
    count=s.count(char) 
    print(char+": "+str(count)) 
    
# 

s="banana"
freq={}

for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 
        
for char, count in freq.items():
    print(char + ": " + str(count))
    
#
s="banana"
freq = {} 

for char in s:
    freq[char] = freq.get(char, 0) + 1 
for k, v in freq.items():
    print(k, ":", str(v))


#
s="banana"
freq={}
i=0
while i<len(s):
    char=s[i] 
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 
    i+=1 
    
for char, count in freq.items():
    print(char + ": " + str(count))

    
    
    
    
    