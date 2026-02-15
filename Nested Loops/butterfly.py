n=int(input())
for i in range(1,n+1):
    stars="* "*i   
    hollow_spaces="  "*(2*(n-i))
    print(stars+hollow_spaces+stars)
for i in range(1,n+1):
    stars="* "*(n-i+1)
    hollow_spaces="  "*(2*(i-1))
    print(stars+hollow_spaces+stars)
    