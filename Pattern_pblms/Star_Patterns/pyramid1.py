
n=4 

for i in range(n):
    print(" "*i + "* "*(n-i)) 
    

# 
n=4 

for i in range(n):
    new=""
    for j in range(n-i):
        new+="* " 
    print(" "*i + new)


#


n=4 

i=0 
while i<n:

    j=0
    new=""
    while j<n-i:
        new+="* "
        j+=1 

    print(" "*i+new)
    i+=1 


