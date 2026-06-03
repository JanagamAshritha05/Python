# Remove Duplicates 

lst = [1, 2, 2, 3, 3, 3, 4] 

new=[]

for i in lst:
    if i not in new:
        new.append(i) 
print(new)

# 
lst = [1, 2, 2, 3, 3, 3, 4]

res = []
i = 0

while i < len(lst):
    if lst[i] not in res:
        res.append(lst[i])
    i += 1

print(res)

#
lst = [1, 2, 2, 3, 3, 3, 4]

res = list(set(lst))

print(res)





