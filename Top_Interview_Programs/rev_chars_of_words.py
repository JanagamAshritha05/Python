s="Python is very easy".split()
res=""
for word in s:
    new=""
    for char in word:
        new=char+new
    res+=new+" "
print(res)


###
s="Python is very easy".split()
new=""

for word in s:
    word=word[::-1] 
    new+=word + " "
print(new)


### 
s = "Python is very easy"

res = ""      
word = ""     

for char in s:
    if char != " ":
        word = char + word     
    else:
        res = res + word + " " 
        word = ""            

res+=word
print(res)

    

