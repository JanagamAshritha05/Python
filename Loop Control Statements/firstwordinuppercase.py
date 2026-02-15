string=input()
index=0
for char in string:
    if char==" ":
        break 
    index+=1  
sentence=string[:index].upper()
new_sentence=sentence+string[index:]
print(new_sentence)
# python is programmimg language // PYTHON is a programming language
