# Second Largest 

lst = [3, 1, 4, 1, 5, 9, 2, 6] 


first  = float('-inf')   # -infinity (smaller than ALL numbers)
second = float('-inf')

for i in lst: 
    if i > first:
        second = first  
        first = i 
    elif i > second and i != first:
        second = i 
    
print(second)


# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.sort()
print(lst[-2]) 

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]

largest = second = float('-inf')

i = 0

while i < len(lst):
    num = lst[i]

    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

    i += 1

print(second) 


