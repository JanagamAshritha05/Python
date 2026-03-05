
n=5

for i in range(1, n+1):
    stars1="* "*i 
    print(stars1 + "  "*(n*2 - 2*i) + "* "*i)


for i in range(1, n):
    stars1="* "*(n-i) 
    print(stars1 + "  "*2*i + "* "*(n-i))



# 
n=5

i=1 
while i<=n:
    print("* "*i + "  "*(n*2-2*i) + "* "*(i)) 
    i+=1 

i=1 
while i<n:
    print("* "*(n-i) + "  "*(2*i) + "* "*(n-i)) 
    i+=1 


# 
n=5

for i in range(1, n+1):
    row=""
    for j in range(1, i+1):
        row+="* " 
    print(row + "  "*(n*2 - 2*i) + row)


for i in range(1, n):
    row="" 
    for j in range(1, n-i+1):
        row+="* " 
    print(row + "  "*(2*i) + row) 
    
    

