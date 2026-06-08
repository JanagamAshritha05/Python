# Find Second smallest number 

arr = (10, 20, 50, 30, 40) 

first_small = second_small = float("inf")

for i in arr:
    
    if i < first_small:
        second_small = first_small
        first_small = i 
    
    elif i < second_small and i!=first_small:
        second_small=i 

print(second_small)



# 
arr = (10, 20, 50, 30, 40) 

first_small = second_small = float("inf")

i = 0 

while i<len(arr):

    if arr[i] < first_small:
        second_small = first_small
        first_small = arr[i] 
    
    elif arr[i] < second_small and arr[i]!=first_small:
        second_small = arr[i] 

    i+=1 

print(second_small)



