#Delete by Index

lst = [1, 2, 3, 4, 5]
del lst[2]
print(lst) 

#
lst = [1, 2, 3, 4, 5]
lst.pop(2)
print(lst) 

# 
lst = [1, 2, 3, 4, 5]
lst = [lst[i] for i in range(len(lst)) if i != 2]
print(lst)


