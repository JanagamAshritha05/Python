n=int(input()) 
m=n*2
for i in range(1,n+1):
    if i==1:
        print("*"+"  "*(m-2)+" *")
    elif i==n:
        print("* "*m)
    else:
        print("*"+"  "*(i-2)+" *"+"  "*(m-2*i)+" *"+"  "*(i-2)+" *")
        