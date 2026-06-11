lst = [2, 7, 5, 4, 11, 15]
target = 9 

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            pair = lst[i], lst[j] 
            indexes = i, j 

            print(indexes)



# 
lst = [2, 7, 11, 15]
target = 9

d = {}

for i in range(len(lst)):
    d[lst[i]] = i

for i in range(len(lst)):
    complement = target - lst[i]

    if complement in d and d[complement] != i:
        print([i, d[complement]])
        break 
    
    


