n=int(input())
print("* "*n)
for i in range(1,n-1):
    hollow_spaces="  "*(n-i-2)
    print("* "+hollow_spaces+"*")
print("*")
