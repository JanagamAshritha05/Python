# reveresed() 

lst = [1, 2, 3, 4, 5]
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=" ")

# 
lst = [1, 2, 3, 4, 5]
for i in reversed(lst):
    print(i, end=" ")

# 
lst = [1, 2, 3, 4, 5]
print(*lst[::-1])


