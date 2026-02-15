x=int(input())
n=int(input()) 
sum = 0
for i in range(n):
    power = 2*i + 1
    term = x ** power
    sum += term
print(sum)

#second solution 
x=int(input()) 
n=int(input()) 
sum=0 
power=1 
for i in range(1,n+1):
    term=x**power 
    sum+=term 
    power+=2 
print(sum)