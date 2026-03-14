
s="Hello Python"
print(s[::-1])

# 
s="Hello Python"
print("".join(reversed(s)))

#
s="Hello Python"
rev=""
for char in s:
    rev=char+rev 
print(rev)

#
s="Hello Python"
rev=[]
for char in s:
    rev.insert(0, char)
res="".join(rev)
print(res)

