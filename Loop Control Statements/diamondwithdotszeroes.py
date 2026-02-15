n=int(input())
for i in range(1,n+1):
    dots=". "*(n-i+1)
    zeroes="0 "*(2*i-1)
    print(dots+zeroes+dots)
for i in range(1,n+1):
    dots2=". "*(i)
for j in range(1,n+3):
    zeroes="0 "*(n-j+3)
    left_spaces=" "*i 
    print(left_spaces+zeroes+left_spaces)
    
n=int(input())
h=-1
for i in range(1,n+1):
   c=n-i   
   h=h+2  
   print(". "*c+"0 "*h+". "*c)
for j in range(1,n):
    h=h-2  
    print(". "*j+"0 "*h+". "*j)
    
    