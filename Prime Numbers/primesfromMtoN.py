m=int(input()) 
n=int(input()) 
new=""
for i in range(m,n+1):
    factor=0 
    for j in range(1,i+1):
        if i%j==0:
            factor+=1 
    if factor==2:
        new+=str(j)+" "
if len(new)>0:
    print(new)
else:
    print("No Prime Numbers Found")
    
    