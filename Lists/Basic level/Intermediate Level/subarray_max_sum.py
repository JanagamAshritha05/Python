# Maximum contiguous subarray sum.

lst = [2, -4, 5, -1, 2, -3]

max_sum = float('-inf') 

for i in range(len(lst)):
    total = 0 

    for j in range(i, len(lst)):

        total+=lst[j] 
        
        if total > max_sum:
            max_sum = total 

print(max_sum)


# 
lst = [2, -4, 5, -1, 2, -3]

curr_sum = 0
max_sum = float('-inf')

for num in lst:

    curr_sum += num

    max_sum = max(max_sum, curr_sum)

    if curr_sum < 0:
        curr_sum = 0

print(max_sum)




