#write a program that reads a 4-digit armstrong number and checks if N is an armstrong number.
m=input()
n=len(m)
sum=0
for i in m:
    i=int(i)**n  
    sum+=i 
if sum==int(m):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    