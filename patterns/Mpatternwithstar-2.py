n=int(input()) 
for i in range(1,n+1):
    hollow_spaces="  "*(n-i)
    left_spaces=" "*(n-i)
    print(left_spaces+"* "*i+hollow_spaces+"* "*i)
    
    