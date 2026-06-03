# Second Smallest 

lst = [3, 1, 4, 1, 5, 9, 2, 6] 

smallest = second = float("inf") 

for i in lst:
    if i < smallest:
        second = smallest 
        smallest = i 
    elif i < second and i!=smallest:
        second = i 

print(second)

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]

unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

unique.sort()

print(unique[1]) 

# 
lst = [3, 1, 4, 1, 5, 9, 2, 6]

smallest = second = float('inf')

i = 0

while i < len(lst):
    num = lst[i]

    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num

    i += 1

print(second) 



