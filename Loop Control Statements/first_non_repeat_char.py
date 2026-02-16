## finding first non-repeating character in a string 

s= "programming" # // p 

new=""
res=[]
for char in s:
    if char not in new:
        new+=char 

for char in new:
    count=s.count(char)
    if count==1:
        res.append(char) 

print(res[0])

# 
s="programmimg"

for char in s:
    if s.count(char)==1:
        print(char)
        break 


# 
s = "programming"

for char in s:
    if s.index(char) == s.rindex(char):
        print(char)
        break

#

s="programming"

freq={}

for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 

for char in s:
    if freq[char]==1:
        print(char)
        break 
    
