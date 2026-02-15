string=input() 
new_str=string.lower() 
char=""
for i in new_str:
    char=i+char 
    if char==new_str:
        res="True" 
    else:
        res="False" 
print(res)
