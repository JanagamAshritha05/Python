s = "aaabbccccdde"

res=[]
count=1 

for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count+=1 
    else:
        res.append(count) 
        count=1

res.append(count) 

res.sort()
print(res[len(res)-1])


## 
s="aaabbccccdde"

max_len=1 
count=1 

for i in range(1, len(s)):
    if s[i]==s[i-1]:
        count+=1 
    else:
        if count>max_len:
            max_len=count 
        count=1 

if count>max_len:
    max_len=count 

print(max_len)

