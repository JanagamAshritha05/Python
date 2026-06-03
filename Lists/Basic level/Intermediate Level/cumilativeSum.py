'''
Cumulative Sum 

Input:  [1, 2, 3, 4, 5]
Output: [1, 3, 6, 10, 15]

'''

lst = [1, 2, 3, 4, 5]
sum=0 
res=[]
for i in lst:
    sum+=i 
    res.append(sum)
print(res)


#
lst = [1, 2, 3, 4, 5]

res = []
total = 0

i = 0

while i < len(lst):
    total += lst[i]
    res.append(total)
    i += 1

print(res)

#



