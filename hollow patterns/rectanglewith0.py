m=int(input())
n=int(input())
for i in range(1, m+1):
    if i==1 or i==m:
        print("* "*n)
    else:
        print("* "+"0 "*(n-2)+"*")
        
        
        