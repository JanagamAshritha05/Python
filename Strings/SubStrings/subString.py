
s="abc"

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])


#
s="abc"
res=[]

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        res.append(s[i:j]) 
print(res)
    

#
s="abc"
i=0 
while i<len(s):
    j=i+1 
    while j<=len(s):
        print(s[i:j])
        j+=1 
    i+=1 


'''
Find all substrings of a string
i/p:abc  o/p:   a
                ab
                abc
                b
                bc
                c

'''


