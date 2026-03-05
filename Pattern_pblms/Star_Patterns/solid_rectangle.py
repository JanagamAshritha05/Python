
m=3 
n=6 

for i in range(m):
    row="" 
    for j in range(n):
        row+="* " 
    print(row) 


# 
m=3 
n=6 

for i in range(m):
    print("* "*n)


# 
m=3 
n=6 

i=0 
while i<m:
    row="" 
    j=0 
    while j<n:
        row+="* " 
        j+=1 
    print(row) 
    i+=1 


