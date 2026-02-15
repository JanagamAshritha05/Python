n=int(input())
for i in range(1,n+1):
    left_spaces=" "*(n-i)
    new_num=""
    for j in range(1,i+1):
        new_num+=str(j)+" "
    print(left_spaces+new_num)
for i in range(1,n):
    left_spaces=" "*(i)
    new_num=""
    for j in range(1,n-i+1):
        new_num+=str(j)+" "
    print(left_spaces+new_num)

#second approach    
n = int(input())
for i in range(1,n):
    spacess = " "*(n-i)
    pattern = ""
    for k in range(1,i+1):
        pattern = pattern+str(k)+" "
    print(spacess+pattern)
for row in range(1,n+1):
    i = n-(row-1)
    spacess = " "*(n-i)
    pattern =""
    for k in range(1,i+1):
        pattern = pattern+str(k)+" "
    print(spacess+pattern)
            
    