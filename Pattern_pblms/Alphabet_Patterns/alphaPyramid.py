

n=5
order=65 
for i in range(1, n+1):
    row="" 
    for j in range(i):
        row=chr(order+j) + " " + row 
    print(" "*(n-i) + row)

# 
n=5 
order=65 
i=1 
while i<=n:
    row="" 
    j=0 
    while j<i:
        row=chr(order + j) + " " + row
        j+=1 
    print(" "*(n-i) + row)
    i+=1 
    
    
    
    
    


