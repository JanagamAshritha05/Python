
d = {"a": 1, "b": 2, "c": 3} 

res = {}

for k, v in d.items():
    res[v] = k 

print(res) 


# 
d = {"a": 1, "b": 2, "c": 3} 

res = {v : k for k, v in d.items()} 

print(res) 

# 
d = {"a": 1, "b": 2, "c": 3} 

res = dict(zip(d.values(), d.keys()))

print(res) 




