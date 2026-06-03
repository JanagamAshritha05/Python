#Maximum in List 

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(max(lst))

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]
maximum = lst[0]
for i in lst:
    if i > maximum:
        maximum = i
print(maximum)

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()
print(lst[-1])


