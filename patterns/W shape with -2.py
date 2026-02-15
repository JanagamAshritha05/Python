n=int(input())
for i in range(1,n+1):
    if i==1:
        print("* "*(2*n-1))
for i in range(1,n):
    left_spaces=" "*(i)
    hollow_spaces="  "*(i-1)
    stars="* "*(n-i)
    print(left_spaces+stars+hollow_spaces+stars)
    
#second solution
n=int(input())
print("* "*(2*n-1))
for i in range(1,n):
    print(" "*i,end="")
    print("* "*(n-i),end="")
    print("  "*(i-1),end="")
    print("* "*(n-i),end="")
    print()