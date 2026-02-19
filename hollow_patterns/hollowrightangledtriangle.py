n=int(input())
for i in range(0,n):
    if i==0:
        print("*")
    elif i==n-1:
        print("* "*n)
    else:
        hollow_spaces="  "*(i-1) 
        print("*"+hollow_spaces+" *")
        