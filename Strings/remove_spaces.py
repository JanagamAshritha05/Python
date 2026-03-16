
s="Hello world"
print(s.replace(" ", ""))

# 
s="Hello world" 
new=""
for char in s:
    if char==" ":
        continue 
    else:
        new+=char 

print(new)

# 
s="Hello world" 
new=""
i=0 
while i<len(s):
    if s[i]==" ":
        i+=1
        continue
    else:
        new+=s[i] 
        i+=1 
    
print(new)    

    
    
    


