string=input()
new=""
for i in string:
    if i==" ":
        new+=" "
        continue
    char=ord(i)+1  
    new_char=chr(char)
    new+=new_char  
print(new)
