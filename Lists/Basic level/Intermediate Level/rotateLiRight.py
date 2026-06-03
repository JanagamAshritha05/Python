# Rotate List to Right 

lst = [1, 2, 3, 4, 5]
k = 2

res = lst[-k:] + lst[:-k]
print(res) 

#
lst = [1, 2, 3, 4, 5]
k = 2

res = []

for i in range(len(lst)-k, len(lst)):
    res.append(lst[i])

for i in range(len(lst)-k):
    res.append(lst[i])

print(res)

# 
lst = [1, 2, 3, 4, 5]
k = 2

res = []

i = len(lst) - k
while i < len(lst):
    res.append(lst[i])
    i += 1

i = 0
while i < len(lst) - k:
    res.append(lst[i])
    i += 1

print(res)



