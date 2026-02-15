n=int(input()) 
for i in range(1,n+3):
    if i==1 or i==n+2:
        print("+ "+"- "*n+"+")
    else:
        print("|"+" "*(2*n+1)+"|")
        