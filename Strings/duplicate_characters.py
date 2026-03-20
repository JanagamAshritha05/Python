
s="programming"    
new=""

for char in s:
    count=s.count(char) 
    if count>1:
        new+=char

for char in set(new):
    print(char)

    
#
s="programming"
freq={}
count=0
for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 

for char, count in freq.items():
    if count>1:
        print(char)
    
    
#
s = "programming"
freq = {}
i = 0
while i < len(s):
    char = s[i]
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
    i += 1

for char, count in freq.items():
    if count > 1:
        print(char)








