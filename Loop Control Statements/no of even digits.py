n=input() 
even=0
for i in n:
    if int(i)%2==0:
        even+=1 
if even>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
    
#256789
