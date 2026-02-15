n=int(input())
for i in range(0,n):
    if i==0:
        print("  "*(n-1)+"*")
    elif i==n-1:
        print("* "*n)
    else:
        left_spaces="  "*(n-i-1)+"* "*i
        print(left_spaces+"*")
        
        