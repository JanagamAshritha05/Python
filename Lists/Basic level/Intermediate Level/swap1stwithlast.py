'''
Swap First and Last 

Input:  [1, 2, 3, 4, 5]
Output: [5, 2, 3, 4, 1]

'''

lst = [1, 2, 3, 4, 5] 

lst[0], lst[-1] = lst[-1], lst[0] 

print(lst)

# 
lst = [1, 2, 3, 4, 5]

temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp

print(lst)

#
lst = [1, 2, 3, 4, 5]

res = [lst[-1]] + lst[1:-1] + [lst[0]]

print(res) 



