m=int(input())              #   7           
n=int(input())              #   4
sum=0                       #   
for i in range(1,n+1):      #"7"+"77"+"777"+"7777"=8638
    i=str(m)*i 
    i=int(i)
    sum+=i 
print(sum)



