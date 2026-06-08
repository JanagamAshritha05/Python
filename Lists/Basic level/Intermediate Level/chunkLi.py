'''
Chunk List 

Input:  [1, 2, 3, 4, 5, 6, 7, 8, 9]  chunk=3
Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3

res = []

for i in range(0, len(lst), k):
    res.append(lst[i:i+k])

print(res)


#
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3 

res = []
temp = []

for num in lst:
    temp.append(num) 

    if len(temp) == k:
        res.append(temp) 
        temp=[]

if temp: 
    res.append(temp)

print(res)


#
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3 

res = []

i = 0 

while i<len(lst):
    res.append(lst[i:i+k])

    i+=k 
    
print(res)




