# Flattened List 

lst = [[1, 2], [3, 4], [5, 6]]

res = []

for sublist in lst:
    for num in sublist:
        res.append(num)

print(res)

#
lst = [[1, 2], [3, 4], [5, 6]]

res = [num for sublist in lst for num in sublist]

print(res)

#
lst = [[1, 2], [3, 4], [5, 6]]

res = []

i = 0
while i < len(lst):

    j = 0
    while j < len(lst[i]):
        res.append(lst[i][j])
        j += 1

    i += 1

print(res)

# 
lst = [[1, 2], [3, 4], [5, 6]]

res = []

for sublist in lst:
    res += sublist

print(res)

