n=int(input()) 
for i in range(1,n+1):
    left_spaces=" "*(n-i)
    if i==n:
        print(left_spaces+"#"*n)
    else:
        print(left_spaces+"*"*i)
        