#Concatenate Two Lists 

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2) 

#
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)

# 
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print([*lst1, *lst2])


