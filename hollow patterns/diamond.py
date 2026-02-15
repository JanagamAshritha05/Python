n=int(input())
for i in range(1,n+1):
    left_spaces=" "*(n-i)
    if i>2 and i<=n:
        hollow_spaces="  "*(i-2)
        print(left_spaces+"*"+hollow_spaces+" *")
    else:
        print(left_spaces+"* "*i)
for i in range(1,n):
    if i==n-1:
        left_spaces=" "*(n-1)
        print(left_spaces+"*")
    else:
        left_spaces=" "*i   
        hollow_spaces="  "*(n-i-2)
        print(left_spaces+"*"+hollow_spaces+" *")
        
#second approach  
n=int(input())
left_spaces_count=n-1  
left_spaces=" "*left_spaces_count  
row_output=left_spaces+"*"
print(row_output)

hollow_spaces_count=-1  
for row in range(2,n+1):
    left_spaces_count=n-row  
    left_spaces=" "*left_spaces_count  
    hollow_spaces_count=hollow_spaces_count+2  
    hollow_spaces=" "*hollow_spaces_count
    row_output=left_spaces+"*"+hollow_spaces+"*"
    print(row_output)
    
for row_bottom in range(1,n-1):
    left_spaces_count=row_bottom  
    left_spaces=" "*left_spaces_count  
    hollow_spaces_count=hollow_spaces_count-2  
    hollow_spaces=" "*hollow_spaces_count  
    row_output=left_spaces+"*"+hollow_spaces+"*"
    print(row_output)
    
left_spaces_count=n-1  
left_spaces=" "*left_spaces_count  
row_output=left_spaces+"*"
print(row_output)


