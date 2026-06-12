'''
Arrange student names in Ascending order

Anand,Ramesh,Kiran
ID102,ID101,ID100

o/p:  
Anand ID102
Kiran ID100
Ramesh ID101

'''

names = ['Anand', 'Ramesh', 'Kiran']
ids = ['ID102', 'ID101' , 'ID100']


res = {}


for i in range(len(names)):
    res[names[i]] = ids[i]

res = (list(res.items()))

for i in range(len(res)):
    for j in range(i+1, len(res)):
        if res[i][0] > res[j][0]:
            res[i], res[j] = res[j], res[i]

for item in res:
    print(*item) 


# 
names = ['Anand', 'Ramesh', 'Kiran']
ids = ['ID102', 'ID101', 'ID100'] 

res = sorted(zip(names, ids)) 

for item in res:
    print(*item)

# 
names = ['Anand', 'Ramesh', 'Kiran']
ids = ['ID102', 'ID101', 'ID100']

res = dict(zip(names, ids)) 
res = sorted(res.items()) 

for i in res:
    print(*i)  


    




