
s="abcdef"
k=3 

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub=s[i:j]
        if len(sub)==3:
            print(sub)


# 
s="abcdef"
k=3 
i=0
while i<len(s):
    j=i+1
    while j<=len(s):
        sub=s[i:j]
        if len(sub)==3:
            print(sub)
        j+=1 
    i+=1 
    

'''
Print substrings of length k

Input: "abcdef", k=3

Output:
abc
bcd
cde
def

'''

