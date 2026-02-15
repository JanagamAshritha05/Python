m=int(input())
n=int(input())
even=0  
odd=0
for i in range(m,n+1):
    if i%2==0:
        even+=1 
    else:
        odd+=1  
print(odd)
print(even)

#print evens and odds in the range from M to N