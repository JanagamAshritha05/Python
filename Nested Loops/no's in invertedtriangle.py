n=int(input())
for i in range(1,n+1):
   num=""
   for j in range(1,n-i+2):
       num+=str(j)+" "
   print(num)
       
