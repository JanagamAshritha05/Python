n=int(input())

for i in range(1,n+1):
    if i==1:
        print("*"*(n*2-1))
    else:
        left_spaces=" "*(i-1)
        print(left_spaces+"*"*(n*2-i*2+1))
        
        