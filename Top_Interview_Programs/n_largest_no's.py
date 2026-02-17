l = [10, 45, 3, 99, 23]
n = 3
    
result = []

for i in range(n):
    max_val = l[0]
    for num in l:
        if num > max_val:
            max_val = num
    result.append(max_val)
    l.remove(max_val)

print(result)

