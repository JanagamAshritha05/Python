'''
Replace element 

Input:  [1, 2, 3, 2, 4, 2]  replace 2 with 9
Output: [1, 9, 3, 9, 4, 9]

'''

lst = [1, 2, 3, 2, 4, 2]

for i in range(len(lst)):
    if lst[i]==2:
        lst[i]=9 
print(lst)


#
lst = [1, 2, 3, 2, 4, 2]

res = []

for num in lst:
    if num == 2:
        res.append(9)
    else:
        res.append(num)

print(res)

#
lst = [1, 2, 3, 2, 4, 2]

i = 0

while i < len(lst):
    if lst[i] == 2:
        lst[i] = 9
    i += 1

print(lst) 

#

lst = [1, 2, 3, 2, 4, 2]

res = [9 if num == 2 else num for num in lst]

print(res)


