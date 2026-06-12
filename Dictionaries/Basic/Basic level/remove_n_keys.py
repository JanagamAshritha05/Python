alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
} 

n = ['a', 'd', 'g'] 

dict = {}

for k, v in alphabets.items():
    if k not in n:
        dict[k] = v 

print(dict) 

# 
alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
} 

n = ['a', 'd', 'g']  

res = {k: v for k, v in alphabets.items() if k not in n}

print(res) 



