n=int(input())
for i in range(1,n+1):
    dots=". "*(n-i)
    zeroes="0 "*(2*i-1)
    print(dots+zeroes+dots)
    
#second approach
n=int(input())
for i in range(n):
    j=i+1 
    m=1+(2*i) 
    print(". "*(n-j)+"0 "*m+". "*(n-j))
    