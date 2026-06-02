# Minimum in List 

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(lst))

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]
minimum = lst[0]
for i in lst:
    if i < minimum:
        minimum = i
print(minimum)

#
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()
print(lst[0])


