'''
Sum of Digits in List 

Input:  [123, 456, 789]
Output: [6, 15, 24]

'''

lst = [123, 456, 789]
res=[]
for num in lst:
    tot=0 
    for i in str(num):
        tot+=int(i) 
    res.append(tot)
print(res)

#
lst = [123, 456, 789]

res = [sum(int(digit) for digit in str(num)) for num in lst]

print(res)




