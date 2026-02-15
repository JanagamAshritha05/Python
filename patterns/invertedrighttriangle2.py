n=int(input()) 
for i in range(1,n+1):
    left_spaces="  "*(i-1)
    numbers=(str(n+1-i)+" ")*(n+1-i)  
    print(left_spaces+numbers)
    