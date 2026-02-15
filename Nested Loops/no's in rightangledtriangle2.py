n=int(input()) 
for i in range(1,n+1):
    spaces="  "*(n-i)
    new=""
    for j in range(1,i+1):
        new=str(j)+" "+new
    print(spaces+new) 
    
    