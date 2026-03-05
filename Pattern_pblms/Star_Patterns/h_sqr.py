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


n = 5 

for i in range(1, n+1):
    row=""
    for j in range(1, n+1):
        if i==1 or i==n:
            row+="* " 
        elif j==1 or j==n:
            row+="* " 
        else:
            row+="  " 
    print(row)
        

# 



n=5 

i=1 

while i<=n:
    row=""
    j=1
    while j<=n:
        if i==1 or i==n:
            row+="* " 
        elif j==1 or j==n:
            row+="* " 
        else:
            row+="  "
        j+=1 
    print(row) 
    i+=1 


    





