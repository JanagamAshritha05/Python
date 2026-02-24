
n = 5 

for i in range(1, n+1):
    print("* "*i) 


for i in range(1, n):
    print("* "*(n-i))


#

n = 5 

i=1 
while i<=n:
    print("* "*i) 
    i+=1 

i=1 
while i<n:
    print("* "*(n-i)) 
    i+=1 


#

n=5 
for i in range(1, n+1):
    row="" 
    for j in range(1, i+1):
        row+="* " 
    print(row)


for i in range(1, n):
    row="" 
    for j in range(1,n-i+1):
        row+="* " 
    print(row)
    

#
n=5 

i=1 
while i<=n:
    row="" 
    j=1
    while j<=i:
        row+="* " 
        j+=1 
    print(row)
    i+=1 

i=1 
while i<n:
    row=""
    j=1 
    while j<=n-i:
        row+="* " 
        j+=1 
    print(row)
    i+=1 





