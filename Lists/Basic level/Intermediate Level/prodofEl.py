'''
Product of digits of each number 

'''

lst = [123, 456]
res=[]

for num in lst:
    prod=1
    for i in str(num):
        prod*=int(i) 
    res.append(prod) 
print(res)

# 


