# print only the positive numbers. 

lst = [-3, -2, -1, 0, 1, 2, 3]
new=[]
for i in lst:
    if i>0:
        new.append(i) 
print(new)

#
lst = [-3, -2, -1, 0, 1, 2, 3]

res = [num for num in lst if num > 0] 

print(res)

#
lst = [-3, -2, -1, 0, 1, 2, 3]

res = []
i = 0

while i < len(lst):
    if lst[i] > 0:
        res.append(lst[i])
    i += 1

print(res) 


