n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*n)
    else:
        hollow_spaces="  "*(n-2)
        print("*"+hollow_spaces+" *")
for i in range(1,n):
    if i==n-1:
        print("* "*n)
    else:
        hollow_spaces="  "*(n-2)
        print(hollow_spaces+"  *")
        
n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n)
    else:
        print("* "+"  "*(n-2)+"*")
for i in range(1,n):
    if i!=n-1:
        print("  "*(n-1)+"*")
    else:
        print("* "*n)
        