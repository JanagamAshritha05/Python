m=int(input())
n=int(input())
print("* "*n)
for i in range(m-2):
    hollow_spaces="  "*(n-2)
    print("* "+hollow_spaces+"* ")
print("* "*n)
