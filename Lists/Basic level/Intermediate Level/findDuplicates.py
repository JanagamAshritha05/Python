#  Find Duplicates 

lst = [1, 2, 2, 3, 3, 3, 4] 

res = []

for i in lst:
    if lst.count(i) > 1 and i not in res:
        res.append(i) 

print(res)

#
lst = [1, 2, 2, 3, 3, 3, 4]

seen = []
dup = []

for num in lst:
    if num not in seen:
        seen.append(num)
    elif num not in dup:
        dup.append(num)

print(dup)

# 
lst = [1, 2, 2, 3, 3, 3, 4]

seen = []
dup = []

i = 0

while i < len(lst):
    if lst[i] not in seen:
        seen.append(lst[i])
    elif lst[i] not in dup:
        dup.append(lst[i])

    i += 1

print(dup) 

