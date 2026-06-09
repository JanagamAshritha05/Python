'''
Maximum contiguous array 

lst = [2, -4, 5, -1, 2, -3]
o/p: [5, -1, 2]

'''

lst = [2, -4, 5, -1, 2, -3]

max_val = float("-inf")

for i in range(len(lst)):

    total = 0 

    for j in range(i, len(lst)):
        total+=lst[j]
    
        if total > max_val:
            max_val = total 
            res = lst[i: j+1] 

print(res)

# 

lst = [2, -4, 5, -1, 2, -3]

max_val = float("-inf") 

i = 0 
while i < len(lst):
    total = 0 
    j = i 
    while j < len(lst):
        total += lst[j]

        if total > max_val:
            max_val = total 
            res = lst[i : j+1] 
        j+=1 

    i+=1 

print(res)






