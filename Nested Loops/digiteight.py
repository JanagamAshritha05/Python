n=int(input())
for i in range(0,n):
    if i==0:
        print("* "*n)
    elif i==n:
        print("* "*n)
    else:
        hollow_spaces="  "*(n-2)
        print("*"+hollow_spaces+" *")
for i in range(1,n+2):
    if i==1:
        print("* "*n)
    elif i==n+1:
        print("* "*n)
    else:
        hollow_spaces="  "*(n-2)
        print("*"+hollow_spaces+" *")

#second solution        
n = int(input())
no_of_rows = (2*n) + 1
for i in range(1, no_of_rows+1):
    if (i == 1) or (i == (n+1)) or (i == no_of_rows):
        print("* " * n)
    else:
        spaces = "  " * (n-2)
        print("* " + spaces + "* ")

        
        
        
        
    