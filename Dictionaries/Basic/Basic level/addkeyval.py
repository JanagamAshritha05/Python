# Add key value pairs 

d = {"a":1, "b":2} 

d["c"] = 3 

print(d) 

#
d = {"a":1, "b":2} 
d.update({"c": 3}) 
print(d)

#
d = {"a":1, "b":2} 
new_d = {}

for k, v in d.items():
    new_d[k] = v 

new_d["c"] = 3 

print(new_d) 



