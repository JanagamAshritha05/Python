n=4

for i in range(n):
    print("  "*i + "* "*(n-i))


# 
n=4 

for i in range(n):
    
    for j in range(n-i+1):
        new="  "*i + "* "*(n-i)
    print(new)


# 
n=4 

for i in range(n):
    new=""
    for s in range(i):     #adding left spaces 
        new+="  "
    for j in range(n-i):   #adding stars 
        new+="* "
    print(new)

        
# 
n=4 

for i in range(n):
    
    for s in range(i):
        print("  ", end="")

    for j in range(n-i):
        print("*", end=" ")
    print()


#  
n=4 

i=0

while i<n:

    s=0 
    while s<i:
        print("  ", end="")
        s+=1 
    
    j=0 
    while j<n-i:
        print("*", end=" ")
        j+=1 
    print()
    i+=1 



