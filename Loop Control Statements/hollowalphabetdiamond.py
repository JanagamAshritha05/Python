n=int(input())
first_char=" "*(n-1)+"A"
print(first_char)
char=66
for i in range(2,n+1):
    left_spaces=" "*(n-i)
    hollow_spaces="  "*(i-2)
    print(left_spaces+chr(char)+hollow_spaces+" "+chr(char))
    char+=1
for i in range(1,n-1):
    left_spaces=" "*(i)
    hollow_spaces="  "*(n-i-2)
    print(left_spaces+chr(char-2)+hollow_spaces+" "+chr(char-2))
    char-=1  
print(first_char)

#second approach  
n=int(input())
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
j=-1 
print(" "*(n-1)+"A")
for i in range(1,n):
    f=n-i-1  
    j=j+2  
    print(" "*f+b[i]+" "*j+b[i]+" "*f)
    h=i  
for k in range(1,n-1):
    j=j-2  
    h=h-1  
    print(" "*k+b[h]+" "*j+b[h])
print(" "*(n-1)+"A")


