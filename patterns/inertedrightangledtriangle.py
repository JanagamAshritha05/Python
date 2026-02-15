n=int(input())
for i in range(1,n+1):
    left_spaces=" "*(i-1)
    m=n-i+1 
    print(left_spaces+str(m)*(n-i+1))
    
    