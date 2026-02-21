n=5 

for i in range(1, n+1):
    if i==1 or i==n:
        print("* "*n)
    else:
        print("* " + "  "*(n-2) + "*")
        

#


n=5 

i=1 
while i<=n:
    if i==1 or i==n:
        print("* "*n)
    else:
        print("* " + "  "*(n-2) + "*")
    i+=1 
    

#
n=5 

for i in range(1, n+1):
    for j in range(1,n+1):
        star1="* "*n 
        star2="  "*(n-2) 
    if i==1 or i==n:
        print(star1)
    else:
        print("* " + star2 +"*")
        

# 


n=5 

i=1 
while i<=n:

    j=0 
    while j<n:
        star1="* "*n 
        star2="* " + "  "*(n-2) + "*" 
        j+=1 
    
    if i==1 or i==n:
        print(star1)
    else:
        print(star2)

    i+=1 

    





