
n=6 

for i in range(1, n+1):
    row="" 
    for j in range(1, n+1):
        if i%2!=0 and j%2!=0:
            row+="* " 
        elif i%2==0 and j%2==0:
            row+="* " 
        else:
            row+=". "
    print(row) 

    
# 
n=6 

i=1 
while i<=n:
    row="" 
    j=1 
    while j<=n:
        if i%2!=0 and j%2!=0:
            row+="* " 
        elif i%2==0 and j%2==0:
            row+="* " 
        else:
            row+=". " 
        j+=1 
    print(row) 
    i+=1 
    
# 
n=6

for i in range(1, n+1):
    if i%2!=0:
        print("* ."*(n//2)) 
    else:
        print(". *"*(n//2)) 
      


