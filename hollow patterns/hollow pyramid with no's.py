n = int(input())

for i in range(1, n+1):
    if i==1:
        print(str(i))
    else:
        print(str(i)+"  "*(i-2)+" "+str(i))
for i in range(1, n):
    if i==n-1:
        print(1)
    else:
        print(str(n-i)+" "*((2*n)-(2*i)-3)+str(n-i))
        
        