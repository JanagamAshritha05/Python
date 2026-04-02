s = "banana"
sub = "ana"

count = 0

for i in range(len(s)-len(sub)+1):
    match=True
    for j in range(len(sub)):
        if s[i+j]!=sub[j]:
            match=False 
            break 
        
    if match:
        count+=1 
        
print(count)


