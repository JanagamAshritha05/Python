s="aba"

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub=s[i:j] 

        if sub==sub[::-1]:
            print(sub)

# 
s="aba"
i=0 
while i<len(s):
    j=i+1
    while j<=len(s):
        sub=s[i:j] 

        if sub==sub[::-1]:
            print(sub)
        j+=1 
    i+=1 


# 
s="aba"
count=0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub=s[i:j] 

        if sub==sub[::-1]:
            count+=1 
print(count)



