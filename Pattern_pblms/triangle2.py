
n = 4 

for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)


# 
n = 4 

for i in range(1,n+1):
    new=""
    for j in range(i):
        new+="* " 
    print("  "*(n-i)+new)
    
#

n = 4 

for i in range(1,n+1):
    for s in range(i):
        if s==0:
            print("  "*(n-i), end="")
    for j in range(i):
        print("*", end=" ")
    print() 


# 
n = 4
i = 1

while i <= n:
    s = 0
    while s < i:
        if s == 0:                  # print spaces only once
            print("  " * (n - i), end="")
        s += 1

    j = 0
    while j < i:
        print("*", end=" ")
        j += 1

    print()
    i += 1



