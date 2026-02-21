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
    for j in range(1,i+1):
        stars1="  "*(n-i) + "* "*i 
        stars2="  "*(n-i) + "* " + "  "*(i-2) + "*"

    if i==1 or i==n:
        print(stars1) 
    else:
        print(stars2)


#
n = 5 

i = 1 

while i<=n:

    j=0 
    while j<i:
        stars1 = "  "*(n-i) + "* "*i 
        stars2 = "  "*(n-i) + "* " + "  "*(i-2) + "*" 
        j+=1 

    if i==1 or i==n:
        print(stars1) 
    else:
        print(stars2) 

    i+= 1 

    
