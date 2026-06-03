'''
Move Zeros to End 

Input:  [0, 1, 0, 2, 0, 3]
Output: [1, 2, 3, 0, 0, 0]

'''
lst = [0, 1, 0, 2, 0, 3] 

res1 = []
res2=[]
for i in lst:
    if i!=0:
        res1.append(i) 
    else:
        res2.append(i) 

print(res1 + res2)

# 
lst = [0, 1, 0, 2, 0, 3]

res = []
count = 0

for num in lst:
    if num == 0:
        count += 1
    else:
        res.append(num)

for i in range(count):
    res.append(0)

print(res)

# 



