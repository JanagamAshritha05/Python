num1=int(input())
num2=int(input())

last_num=num1-1 

for i in range(1,num2+1):
    
    for j in range(1,i+1):
        last_num+=1  
        
for i in range(1,num2+1):
    new_num=""
    for j in range(1,i+1):
        new_num+=str(last_num)+" "
        last_num-=1
    print(new_num)
        