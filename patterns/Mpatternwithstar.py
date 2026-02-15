n=int(input()) 
for i in range(1,n+1):
    hollow_spaces="  "*(n*2-i*2)
    print("* "*i+hollow_spaces+"* "*i)
    