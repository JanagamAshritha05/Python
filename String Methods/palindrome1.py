string=input() 
char=""
for i in string:
    char=i+char 
    if char==string:
        res="True" 
    else:
        res="False" 
print(res) 
