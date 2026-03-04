
n=4
order=65
for i in range(1,n+1):
    row="" 
    for j in range(i):
        row+=chr(order)+" " 
        order+=1
    print(row)
    
# 
n=4 
i=1 
order=65
while i<=n:
    row="" 
    j=0 
    while j<i:
        row+=chr(order)+" " 
        order+=1 
        j+=1
    print(row)
    i+=1

