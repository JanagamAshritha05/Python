lst = [2, 7, 5, 4, 11, 15]
target = 9

d = {}

for i in range(len(lst)):
    d[lst[i]] = i

for i in range(len(lst)):
    complement = target - lst[i]

    if complement in d and d[complement] != i:
        print(lst[i], complement)
        break  


