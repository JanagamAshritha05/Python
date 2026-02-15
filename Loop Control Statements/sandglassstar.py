n=int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"* "*(n-i+1))
for j in range(2,n+1):
    left_spaces=" "*(n-j)
    print(left_spaces+"* "*j)

#second approach    
n=int(input())
for i in range(n):
    left_spaces=" "*i  
    stars="* "*(n-i)
    print(left_spaces+stars)
for i in range(2,n+1):
    left_spaces=" "*(n-i)
    stars="* "*i  
    print(left_spaces+stars)
    
    