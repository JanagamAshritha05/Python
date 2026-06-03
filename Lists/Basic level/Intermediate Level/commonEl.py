'''
Common elements in a list 
Input:  [1, 2, 3, 4, 5]  [3, 4, 5, 6, 7]
Output: [3, 4, 5] 

'''

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

res = []

for num in lst1:
    if num in lst2 and num not in res:
        res.append(num)
print(res)

#
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

res = list(set(lst1) & set(lst2))

print(res) 

#
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

res = []

i = 0

while i < len(lst1):
    if lst1[i] in lst2 and lst1[i] not in res:
        res.append(lst1[i])
    i += 1

print(res)

#


