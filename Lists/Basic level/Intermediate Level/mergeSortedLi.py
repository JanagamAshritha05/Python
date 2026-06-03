'''
Merge two sorted Lists 
Input:  [1, 3, 5, 7]  [2, 4, 6, 8]
Output: [1, 2, 3, 4, 5, 6, 7, 8]

'''

lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]

res = lst1 + lst2
res.sort()

print(res) 

# Using Two Pointers(Merge Sort) 

lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]

i = j = 0
res = []

while i < len(lst1) and j < len(lst2):

    if lst1[i] < lst2[j]:
        res.append(lst1[i])
        i += 1
    else:
        res.append(lst2[j])
        j += 1

while i < len(lst1):
    res.append(lst1[i])
    i += 1

while j < len(lst2):
    res.append(lst2[j])
    j += 1

print(res)


