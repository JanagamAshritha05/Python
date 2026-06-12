'''
Replace key with new Key 

'''
fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
} 

key = 'apples'
new_key = 'pommegranates' 

lst = list(fruits.items()) 

for i in range(len(lst)):
    if lst[i][0] == key:
        updated_key = new_key 
        new_tuple = (updated_key, lst[i][1]) 
        lst[i] = new_tuple 

print(lst) 

# 
fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15
}

old_key = "apples"
new_key = "pomegranates"

result = {}

for k, v in fruits.items():
    if k == old_key:
        result[new_key] = v
    else:
        result[k] = v

print(result)


# 
fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15
}

old_key = "apples"
new_key = "pomegranates"

fruits[new_key] = fruits.pop(old_key)

print(fruits) 




