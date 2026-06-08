# Find second Largest Element 

arr = (10, 20, 50, 30, 40) 

first_max = float("-inf")
second_max = float("-inf") 

for i in arr:
    if i > first_max:
        second_max = first_max
        first_max = i 

    elif i > second_max and i!=first_max:
        second_max = i 

print(second_max)


# 
arr = (10, 20, 50, 30, 40)

first_max = float("-inf")
second_max = float("-inf")

i = 0 
while i < len(arr):
    if arr[i] > first_max:
        second_max = first_max 
        first_max = i 

    elif arr[i] > second_max and i!=first_max:
        second_max = i 

        i+=1 

print(second_max)




