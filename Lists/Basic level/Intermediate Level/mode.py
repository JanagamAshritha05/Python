'''
lst = [6, 3, 9, 3, 6, 6, 5, 9, 3]
o/p: 6 

The numbers 6, 3 occures same number of times, print mode that occurs first 
among 6, 3 the  6 occurs first

'''
lst = [6, 3, 9, 3, 6, 6, 5, 9, 3]  

max_val = 0 
mode = 0

for i in lst:
    val = lst.count(i) 
    if val > max_val:
        max_val = val 
        mode = i 

print(mode)



