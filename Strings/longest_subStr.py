#Find Longest Substring Without Repeating Characters

s="abcabcbb"
new=""
for i in range(len(s)):
    if s[i] in new:
        break
    else:
        new+=s[i] 
print(new)
print(len(new))

#
s="abcabcbb"
max_str=""
for i in range(len(s)):
    new=""
    for j in range(i, len(s)):
        if s[j] in new:
            break 
        else:
            new+=s[j] 
    if len(new)>len(max_str):
        max_str=new 
print(max_str)
print(len(max_str))
        
#
s="abcabcbb"
max_str=""
i=0 
while i<len(s):
    new=""
    j=i 
    while j<len(s):
        if s[j] in new:
            break 
        new+=s[j] 
        j+=1 
    if len(new)>len(max_str):
        max_str=new 
    i+=1 

print(max_str)
print(len(max_str))



