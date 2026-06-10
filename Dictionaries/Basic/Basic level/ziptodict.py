'''
Zip Lists into Dictionary 

keys = ["a", "b", "c"]
values = [1, 2, 3]

o/p:  {"a": 1, "b": 2, "c": 3}

'''

keys = ['a', 'b', 'c'] 
values = [1, 2, 3] 

res = {} 

for i in range(len(keys)):
    res[keys[i]] = values[i] 

print(res) 

# 
keys = ["a", "b", "c"]
values = [1, 2, 3]

res = dict(zip(keys, values)) 

print(res) 

# 
keys = ["a", "b", "c"]
values = [1, 2, 3]

res = {k: v for k, v in zip(keys, values)} 

print(res) 




