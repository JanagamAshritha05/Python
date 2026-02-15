n=int(input()) 
for i in range(1,n+1):
    left_spaces=" "*(i-1) 
    if i==1:
        print(left_spaces+"+ "*(n-i+1))
    else:
        print(left_spaces+"* "*(n-i+1))
        