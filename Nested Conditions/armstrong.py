#Write an armstrong number that reads a three digit number N and checks if N is an armstrong number.
m=input() 
n=len(m)
count=0
for i in m:
    i=int(i)**n  
    count+=i 
if count == int(m):
    print("True")
else:
    print("False")
    
#second answer
X=int(input())
num_str=str(X)
b=int(num_str[0])
c=int(num_str[1])
d=int(num_str[2])
e=(b**3+c**3+d**3)
x=(e==X)
if x:
    print("True")
else:
    print("False")
    

