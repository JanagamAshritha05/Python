# Rotate list left 

lst = [1, 2, 3, 4, 5]
k = 2 

print(lst[k:] + lst[:k])


# 
lst = [1, 2, 3, 4, 5]
k = 2 

res=[]

for i in range(k, len(lst)):
    res.append(lst[i])

for i in range(k):
    res.append(lst[i])

print(res)

# 
lst = [1, 2, 3, 4, 5]
k = 2

res = []

i = k
while i < len(lst):
    res.append(lst[i])
    i += 1

i = 0
while i < k:
    res.append(lst[i])
    i += 1

print(res)

