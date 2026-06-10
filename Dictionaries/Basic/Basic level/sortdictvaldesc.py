d = {"a": 3, "b": 1, "c": 2, "d": 5} 

items = list(d.items())
res = {}

for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i] 

for k, v in items:
    res[k] = v
     
print(res) 


