n=int(input())
for k in range(1,n+1):
    i=n-(k-1)
    left_spaces=" "*(n-i)
    if i>2 and i<n:
        hollow_spaces="  "*(i-2)
        print(left_spaces+"* "+hollow_spaces+"* ")
    else:
        stars="* "*i   
        print(left_spaces+stars)
        
        
        