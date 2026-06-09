# Delete a key 

d = {"a":1, "b":2, "c":3}  

del d["b"]
print(d)

#
d = {"a":1, "b":2, "c":3} 
d.pop("b")
print(d) 

#
d = {"a":1, "b":2, "c":3}
new_d = {}

for k, v in d.items():
    if k!="b":
        new_d[k] = v 

print(new_d) 


