#Access Elements by Index 

lst = [10, 20, 30, 40, 50]
print("First  :", lst[0])
print("Last   :", lst[-1])
print("Middle :", lst[len(lst)//2])

#
lst = [10, 20, 30, 40, 50]
first  = lst[0]
last   = lst[len(lst)-1]
middle = lst[len(lst)//2]
print("First  :", first)
print("Last   :", last)
print("Middle :", middle)

# 
lst = [10, 20, 30, 40, 50]
for i in range(len(lst)):
    if i == 0:
        print("First  :", lst[i])
    elif i == len(lst)//2:
        print("Middle :", lst[i])
    elif i == len(lst)-1:
        print("Last   :", lst[i])

        
