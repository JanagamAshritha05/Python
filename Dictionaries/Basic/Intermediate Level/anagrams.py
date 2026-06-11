d = {
    "eat": 1,
    "tea": 2,
    "tan": 3,
    "ate": 4,
    "nat": 5,
    "bat": 6
} 

res = {}

for k, v in d.items():
    new_key = "".join(sorted(k))

    if new_key in res:
        res[new_key][k] = v 
     
    else:
        res[new_key] = {k:v} 

print(res)



