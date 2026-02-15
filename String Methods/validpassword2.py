string=input() 
res=False 
for i in string:
    if i.isupper():
        res=True 
if res:
    print("Valid Password")
else:
    print("Invalid Password")
    
# print valid if it contains atleast one uppercase
