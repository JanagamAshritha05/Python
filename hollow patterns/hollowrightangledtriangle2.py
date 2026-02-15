n=int(input())
print("_"*(n+1))
for i in range(0,n):
        hollow_spaces=" "*(n-i-1)
        print("|"+hollow_spaces+"/")
        