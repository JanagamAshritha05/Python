s = "aabbbceeeyu" # // a2b3c1e3y1u1

new=""
res=""

for char in s:
    if char not in new:
        new+=char 

for char in new:
    count=s.count(char) 
    res+=char + str(count)

print(res)


# 

s="aabbbceeeyu"

res=""
count=1 

for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count+=1 
    else:
        res+=s[i-1] + str(count) 
        count=1 

res+=s[-1] + str(count) 

print(res)


# 


s="aabbceeeyu"

prev=s[0]
count=1 
res=""

for i in range(1, len(s)):
    if s[i]==prev:
        count+=1 
    else:
        res+=prev + str(count) 
        prev=s[i] 
        count=1 

res+=prev + str(count) 

print(res)


# 
s = "aabbbceeeyu"

res = ""
i = 0

while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    res += s[i] + str(count)
    i += 1

print(res)


