s = "success"

freq={}

for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 


for key, val in freq.items():
    print(str(key) + ": " + str(val))


# 
s="success"
 
new=""

for char in s:
    if char not in new:
        new+=char 

for char in new:
    count=s.count(char) 
    print(char+ ": " +str(count))

