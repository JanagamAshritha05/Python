x=int(input()) 
n=int(input()) 
power=2 
sum=0 
for i in range(1,n+1):
    term=x**power 
    sum+=term 
    power+=2 
print(sum)
 
# 3         ex:    3**2 + 3**4 + 3**6 + 3**8 = 7380
# 4


