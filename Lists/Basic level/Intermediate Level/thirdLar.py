# Third largest 

lst = [3, 1, 4, 1, 5, 9, 2, 6] 

first = second = third = float("-inf")

for i in lst:

    if i > first:
        third = second 
        second = first 
        first = i 

    elif i > second and i!=first:
        third = second 
        second = i 

    elif i > third and i!=second and i!=first:
        third = i 
    
print(third)

#
lst = [3, 1, 4, 1, 5, 9, 2, 6]

unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

unique.sort()

print(unique[-3])

#
lst = [3, 1, 4, 1, 5, 9, 2, 6]

first = second = third = float('-inf')

i = 0

while i < len(lst):

    num = lst[i]

    if num > first:
        third = second
        second = first
        first = num

    elif num > second and num != first:
        third = second
        second = num

    elif num > third and num != second and num != first:
        third = num

    i += 1

print(third)



