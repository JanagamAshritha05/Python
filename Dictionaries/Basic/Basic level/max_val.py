# Find Max Value 

d = {"a":10, "b":50, "c":20} 

print(max(d.values()))

#

d = {"a":10, "b":50, "c":20} 
max_val = float("-inf") 

for val in d.values(): 
    if val > max_val:
        max_val = val  

print(max_val) 


# 
d = {"a":10, "b":50, "c":20} 

max_val = float("-inf")

for k in d:
    if d[k] > max_val:
        max_val = d[k] 

print(max_val) 





