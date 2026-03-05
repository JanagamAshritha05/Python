n = 5 

for i in range(1, n+1):
    if i==1 or i==n:
        print("  "*(n-i) + "* "*i) 
    else:
        print("  "*(n-i) + "* " + "  "*(i-2) + "*")


# 
 
n = 5 

i=1 
while i<=n:
    if i==1 or i==n:
        print("  "*(n-i) + "* "*i)
    else:
        print("  "*(n-i) + "* " + "  "*(i-2) + "*")
    i+=1  

    
#
n = 5
for i in range(1, n+1):
    row=""
    spaces="  "*(n-i) 
    for j in range(1, i+1):
        if i==1 or i==n:
            row+="* " 
        elif j==1 or j==i:
            row+="* " 
        else:
            row+="  " 
    print(spaces + row) 





#
n = 5

i=1 
while i<=n:
    row=""
    spaces="  "*(n-i) 
    j=1 
    while j<=i:
        if i==1 or i==n:
            row+="* " 
        elif j==1 or j==i:
            row+="* " 
        else:
            row+="  "
        j+=1 
    print(spaces + row)
    i+=1 




    
