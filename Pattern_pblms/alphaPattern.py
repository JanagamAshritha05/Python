
n=5 

new="" 
order=65
for i in range(1, n+1):
    new+=chr(order) + " " 
    order+=1 
    print(new) 

    
# 
n=5 

for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end=" ")     
    print()


# 

n=5 

i=1 
while i<=n:
    j=0 
    while j<i:
        print(chr(65 + j), end=" ")
        j+=1
    print() 
    i+=1 



