# Check Element Exists 

lst = [1, 2, 3, 4, 5]
print(3 in lst) 

#
lst = [1, 2, 3, 4, 5]
print(lst.count(3) > 0)

# 
lst = [1, 2, 3, 4, 5]
found=False 
for i in lst:
    if i==3:
        found=True 
        break 
print(found)




