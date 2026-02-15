n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    elif i>=2 and i<n:
        print(" "*(n-i)+"*"+"  "*(i-2)+" *")
        