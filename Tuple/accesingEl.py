# Accessing Nested tuple elements 

list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]

res=[]
n=int(input()) 
for i in range(n):
    num=input().split() 
    index1=int(num[0]) 
    index2=int(num[1]) 
    res.append(list_a[index1][index2])
print(res)


