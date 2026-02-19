n=int(input()) 
m=n*2  
for i in range(1, n+1):
    if i==1:
        print("*"+"  "*(m-2)+" *")
    else:
        print("*"+"  "*(i-2)+" *"+"  "*(m-2*i)+" *"+"  "*(i-2)+" *")
for i in range(1, n+1):
    if i==n:
        print("*"+"  "*(m-2)+" *")
    else:
        print("*"+"  "*(n-i-1)+" *"+"  "*(2*i-2)+" *"+"  "*(n-i-1)+" *")
        
        