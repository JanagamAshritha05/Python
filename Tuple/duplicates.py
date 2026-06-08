
arr = (1, 2, 2, 3, 3, 4) 

seen = []
dup = []

for i in arr:
    if i not in seen:
        seen.append(i)
    elif i not in dup:
        dup.append(i) 

print(tuple(dup)) 



