n=int(input())
k=int(input())
new=[]
factors=0
for i in range(1,n+1):
    if n%i==0:
      factors+=1  
      char=i
      new.append(char)
if factors<k:
    print("1")
else:
    res=sorted(new,reverse=True)
    print(res[k-1])
  
  #i/p: 12  o/p: 4  i/p:  12    o/p:  1
  #     3                 7