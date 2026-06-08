'''
Return the indices of two numbers whose sum equals the target.
[2, 7, 11, 15]   o/p:  [0, 1]
target = 9

'''

lst = [2, 7, 5, 4, 11, 15] 
n = 9 

for i in range(len(lst)):
    for j in range(i+1, len(lst)):

        if lst[i] + lst[j]==n and i<n:
            indices = (i, j) 
            print(indices)





