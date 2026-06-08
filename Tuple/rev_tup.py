# reverse Tuple 

arr = (1, 2, 3, 4) 
res=[]
for i in range(len(arr)-1, -1, -1):
    res.append(arr[i]) 

print(tuple(res))


#
arr = (1, 2, 3, 4) 
res = []
i=len(arr)-1
while i>=0:
    res.append(arr[i])
    i-=1 
print(tuple(res)) 



