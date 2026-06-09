# Prime Numbers in a List 

lst = [1, 2, 3, 4, 5, 6, 7]
new=[]

for i in lst:
    factors = 0 
    for j in range(1, i+1):
        if i%j==0:
            factors+=1 
        
    if factors == 2:
        new.append(i) 

if len(new)>1:
    print(new)
else:
    print("No Prime Numbers Found")



