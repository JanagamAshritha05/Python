
s="I love python".split() 
print(len(s))

# 
s="I love python"
count=0 
in_word=False 
for char in s:
    if char!=" " and in_word==False:
        count+=1 
        in_word=True 
    elif char==" ":
        in_word=False 
    
print(count)

#
s = "I love python"
count = 0
for char in s:
    if char == " ":
        count += 1
count += 1  # add 1 for last word
print(count)





