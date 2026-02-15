n=int(input())
for i in range(1,n+1):
    left_spaces=" "*(n-i)
    if i>2 and i<n:
        hollow_spaces="  "*(i-2)
        print(left_spaces+"1 "+hollow_spaces+str(i)+" ")    
    else:
        new_num=""
        for j in range(1,i+1):
            new_num+=str(j)+" "
        print(left_spaces+new_num)
        