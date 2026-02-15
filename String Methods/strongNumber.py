n="145"
sum=0 
for i in n:
  prod=1 
  for j in range(1,int(i)+1):
    prod*=j 
  sum+=prod 
if sum==int(n):
  print("Strong Number")
else:
  print("Not a Strong Number")
  

