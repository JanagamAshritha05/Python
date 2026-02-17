l = [10, 89, 3, 99, 23]

largest=l[0]
second_largest=-10**9 

for num in l:
    if num>largest:
        second_largest=largest 
        largest=num 
    elif num>second_largest and num!=largest:
        second_largest=num 
        
print(second_largest)

