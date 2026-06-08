'''
Flattened Tuple 
i/p: ((1, 2), (3, 4), (5, 6))  
o/p: (1, 2, 3, 4, 5, 6) 

'''
arr = ((1, 2), (3, 4), (5, 6)) 
lst=[]
for t in arr:
    for num in t:
        lst.append(num)

print(tuple(lst)) 


#
arr = ((1, 2), (3, 4), (5, 6))  

res = tuple((num for t in arr for num in t))

print(res)




