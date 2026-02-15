n=int(input())
for i in range(1,n+1):
    left_spaces=" "*(i-1)
    new_num=""
    for j in range(1,n-i+2):
        new_num+=str(j)+" "
    print(left_spaces+new_num)
    