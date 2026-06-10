'''
merge two dictionaries 

Note: If the same key exists in both dictionaries,
the value from the second dictionary (d2) overwrites the first dictionary
'''

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = {}

for key, value in d1.items():
    result[key] = value

for key, value in d2.items():
    result[key] = value

print(result)


# 
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)

print(d1) 

# 
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = {**d1, **d2}

print(result)


