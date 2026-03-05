 
n = 5 

for i in range(1, n+1):
    if i==1 or i==n:
        print("* "*(n-i+1))
    else:
        print("* " + "  "*(n-i-1) + "*")



# 
 
n = 5 

i = 1

while i<=n:
    if i==1 or i==n:
        print("* "*(n-i+1)) 
    else:
        print("* " + "  "*(n-i-1) + "*")
    
    i+= 1 
    

# 


n = 5

for i in range(1, n+1):
    row="" 
    for j in range(1, n-i+2):
        if i==1 or i==n:
            row+="* " 
        elif j==1 or j==n-i+1:
            row+="* " 
        else:
            row+="  " 

    print(row)
    

#

n = 5
i = 1
while i <= n:
    row = ""
    j = 1
    while j <= n-i+1:
        if i == 1 or i == n:
            row += "* "
        elif j == 1 or j == n-i+1:
            row += "* "
        else:
            row += "  "
        j += 1
    print(row)
    i += 1

    