n=int(input())                  # Print indivisible numbers from 1 to N 
count=0
for i in range(1,n+1):
    factors=0
    for j in range(2,11):
        if i%j==0:
            factors+=1 
    if factors==0:
        count+=1  
print(count)

#second approach
n=int(input())
count=0   
for i in range(1,n+1):
    is_divisible="False"
    for j in range(2,11):
        if i%j==0:
            is_divisible="True"
    if is_divisible=="False":
        count+=1   
print(count)
    
