n=int(input()) 
for i in range(1,n+1):
    left_spaces=" "*(n-i) 
    print(left_spaces+(str(i)+" ")*i)
for i in range(1,n):
    left_spaces=" "*i  
    print(left_spaces+(str(n-i)+" ")*(n-i))
    