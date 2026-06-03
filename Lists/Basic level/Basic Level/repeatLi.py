#Repeat List 

lst = [1, 2, 3]
print(lst * 3) 

#
lst = [1, 2, 3]
print(lst * 3) 

#
lst = [1, 2, 3]
result = []
for i in range(3):
    result += lst
print(result) 

#
lst = [1, 2, 3]
result = [x for x in lst for _ in range(3)]
print(result) 



