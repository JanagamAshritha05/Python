string=input() 
new_str=""
for i in string:
    if i.islower() or i.isupper():
        new_str+=i 
print(new_str) 

#--c--a--r-- // car