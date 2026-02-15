string=input()
new_string1=string.replace(" ","")
new_string2=new_string1.replace("'","")
new_string3=new_string2.lower()
reverse=""
for char in new_string3:
    reverse=char+reverse  
if reverse==new_string3:
    print("True")
else:
    print("False")
    