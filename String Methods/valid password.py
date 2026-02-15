password=input()
res=False 
for char in password:
    if char.isdecimal():
        res=True 
if res:
    print("Valid Password")
else:
    print("Invalid Password")
    
# print valid password if it contains atleast one digit
