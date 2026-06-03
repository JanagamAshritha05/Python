'''
Zip Two Lists 

Input:  [1, 2, 3]  ['a', 'b', 'c']
Output: [(1,'a'), (2,'b'), (3,'c')]

'''

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']

print(list(zip(lst1, lst2)))

# 
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c'] 

res=[]

for i in range(len(lst1)):
    res.append((lst1[i], lst2[i]))
print(res)


# 
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']

res=[]
i=0 

while i<len(lst1):
    res.append((lst1[i], lst2[i]))
    i+=1 
print(res)

#
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c'] 

res = [(lst1[i], lst2[i]) for i in range(len(lst1))]
print(res)


