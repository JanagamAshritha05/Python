
n=5
order=65
for i in range(1, n+1):
    row="" 
    for j in range(i):
        row+=chr(order) + " " 
    print(row) 
    order+=1
        
# 
n=5 
order=65
i=1 
while i<=n:
    row=""
    j=0 
    while j<i:
        row+=chr(order) + " "
        j+=1 
    print(row)
    i+=1
    order+=1

# 
n=5 
order=65
for i in range(1, n+1):
    row=chr(order) + " " 
    print(row*i) 
    order+=1 
    
    
