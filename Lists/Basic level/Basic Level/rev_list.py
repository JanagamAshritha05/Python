# Reverse a List 

lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst) 

#
lst = [1, 2, 3, 4, 5]
print(lst[::-1])

# 
lst = [1, 2, 3, 4, 5]
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)



