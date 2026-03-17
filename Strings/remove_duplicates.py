

s="programming"
new=""
for char in s:
    if char not in new:
        new+=char 
print(new)

#
s="programming"
new=""
i=0 
while i<len(s):
    if s[i] not in new:
        new+=s[i] 
    i+=1 
print(new)

#
s="programming"
freq={}
new=""
for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 

for char, count in freq.items():
    new+=char 
    
print(new)
    
    
    



