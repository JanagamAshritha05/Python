n=int(input())
for i in range(0,n):
    if i==0:
        print("* "*n)
    elif i==n-1:
        print("  "*(n-1)+"*")
    else:
        left_spaces="  "*(i)
        hollow_spaces="  "*(n-i-2)
        print(left_spaces+"* "+hollow_spaces+"*")
        
        
        