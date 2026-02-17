s = "Python is very easy"

in_word=False 
count=0 

for char in s:
    if char!="" and not in_word:
        count+=1 
        in_word=True 
    elif char==" ":
        in_word=False 

print(count)



## 
s="python is very easy".split()
print(len(s))

