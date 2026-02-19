n = int(input())
for i in range(1 , n+1):
    left_spaces = "  " * (n-i)
    if i == 1:
        print(left_spaces + str(i))
    else:
        hollow_spaces = "  " * (i -2)
        print(left_spaces + (str(i) +  " ") + hollow_spaces + str(i))
for i in range(1, n):
    if i == n-1:
        print(("  "*i)+(str(1)+" ")*1)
    elif i==n-2:
        print(("  "*i)+(str(2)+" ")*2)
    else:
        print(("  "*i)+(str(n-i)+" ")+("  "*(n-i-2))+(str(n-i)+" "))
        