n=int(input())
for i in range(1,n+1):
    if i>2 and i<n:
        hollow_spaces="  "*(i-2)
        print("1 "+hollow_spaces+str(i))
    else:
        new_num=""
        for j in range(1,i+1):
            new_num+=str(j)+" "
        print(new_num)
        