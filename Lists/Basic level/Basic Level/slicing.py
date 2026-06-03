# slicing 

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First 3 :", lst[:3])
print("Last 3  :", lst[-3:])
print("Middle  :", lst[3:7]) 

# 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first3 = [lst[i] for i in range(3)]
last3  = [lst[i] for i in range(len(lst)-3, len(lst))]
middle = [lst[i] for i in range(3, 7)]
print("First 3 :", first3)
print("Last 3  :", last3)
print("Middle  :", middle)


