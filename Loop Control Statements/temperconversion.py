a=input()
b=len(a)-1  
h=a[:b]
p=a[b]
if p=="C":
    print(str(float(h))+p)
    f=((float(h)*9)/5)+32  
    print(str(round(f,1))+"F")
    k=float(h)+273  
    print(str(round(k,1))+"K")
if p=="F":
    c=(float(h)-32)*(5/9)
    print(str(round(c,2))+"C")
    print(a)
    k=c+273  
    print(str(round(k,2))+"K")
if p=="K":
    c=float(h)-273  
    print(str(round(c,1))+"C")
    f=((float(c)*9)/5)+32  
    print(str(round(f,1))+"F")
    print(str(float(h))+"K")
    
#i/p: 25C   o/p:    25.0C
#                   77.0F
#                   298.0K
