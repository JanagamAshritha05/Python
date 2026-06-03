'''
Split List into Two Halves

Input:  [1, 2, 3, 4, 5, 6]
Output:
First half  : [1, 2, 3]
Second half : [4, 5, 6]

'''
lst = [1, 2, 3, 4, 5, 6]

mid = len(lst) // 2

first_half = lst[:mid]
second_half = lst[mid:]

print("First half :", first_half)
print("Second half:", second_half)

#
lst = [1, 2, 3, 4, 5, 6]

mid = len(lst) // 2

first_half = []
second_half = []

for i in range(len(lst)):
    if i < mid:
        first_half.append(lst[i])
    else:
        second_half.append(lst[i])

print("First half :", first_half)
print("Second half:", second_half) 

#
lst = [1, 2, 3, 4, 5, 6]

mid = len(lst) // 2

first_half = []
second_half = []

i = 0

while i < len(lst):

    if i < mid:
        first_half.append(lst[i])
    else:
        second_half.append(lst[i])

    i += 1

print("First half :", first_half)
print("Second half:", second_half)



