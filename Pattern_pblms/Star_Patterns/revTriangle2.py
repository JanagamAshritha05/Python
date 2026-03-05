
n=5
order=65 
for i in range(1, n+1):
    row="" 
    for j in range(i):
        row=chr(order + n-j-1) + " " + row
    print(row)

# 
n=5 
order=65 
i=1 
while i<=n:
    row="" 
    j=0 
    while j<i:
        row=chr(order + n-j-1) + " " + row
        j+=1 
    print(row)
    i+=1 
    
    
    
    
    

