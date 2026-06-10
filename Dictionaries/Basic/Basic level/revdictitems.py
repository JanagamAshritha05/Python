d = {"a": 1, "b": 2, "c": 3} 

items = list(d.items())

res = {}

for i in range(len(d)-1, -1, -1):
    k, v = items[i] 
    res[k] = v 

print(res)

# 
d = {"a": 1, "b": 2, "c": 3} 

res = dict(reversed(d.items()))

print(res) 

#
d = {"a": 1, "b": 2, "c": 3} 

res = {k: v for k, v in reversed(d.items())}

print(res) 



