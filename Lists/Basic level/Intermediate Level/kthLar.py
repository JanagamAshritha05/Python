# kth Largest Number 

lst = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3

unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

unique.sort()

print(unique[-k]) 

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]
k = 2 

for i in range(k):
    maximum = float("-inf")
    for j in lst:
        if j > maximum:
            maximum = j 
    lst.remove(maximum)
    res=maximum 

print(res)


