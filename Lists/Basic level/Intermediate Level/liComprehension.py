# List comprehension squares. 

lst = [1, 2, 3, 4, 5] 

res = [i**2 for i in lst] 

print(res)

# 

lst = [1, 2, 3, 4, 5] 
res = []
for i in lst:
    res.append(i*i)
print(res)

# 
lst = [1, 2, 3, 4, 5] 
res=[]
i=0 
while i < len(lst):
    res.append(lst[i]**2) 
    i+=1 
print(res)

# 
lst = [1, 2, 3, 4, 5] 

res=[]

for i in lst:
    res+=[i**2] 
print(res)



