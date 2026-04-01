s="abc"
count=0 

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        count+=1 
print(count)

#
s="abc"
count=0 

i=0
while i<len(s):
    j=i+1 
    while j<=len(s):
        count+=1 
        j+=1 
    i+=1
print(count)


#
s="abc"
n=len(s)
count=(n*(n+1)//2)
print(count)

'''
Input: "abc"
Output: 6
Substrings: a, ab, abc, b, bc, c

'''



