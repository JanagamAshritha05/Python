n=int(input())
for i in range(1,n+1):
    if i==1:
        new_num=""
        for j in range(1,n+1):
            new_num+=str(j)+" "
        print(new_num)
    elif i==n:
        left_spaces=" "*(i-1)
        print(left_spaces+"1 ")
    else:
        left_spaces=" "*(i-1)
        hollow_spaces="  "*(n-i-1)
        print(left_spaces+"1 "+hollow_spaces+str(n-i+1)+" ")
   
#second approach          
n = int(input())
for row in range(1, n+1):
    i = n - (row -1)
    left_spaces = (" " * (row - 1))
    if (i > 2) and (i < n):
        hollow = ("  " * (i - 2))
        numbers = "1 " + hollow + (str(i) + " ")
        print(left_spaces + numbers)
    else:
        numbers = ""
        for j in range(1, i+1):
            numbers = numbers + (str(j) + " ")
        print(left_spaces + numbers)       
        
        
        
        
        
        
        