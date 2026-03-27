s="12345"
if s.isdigit():
    print("True")
else:
    print("False")
    
#
s="12345"
flag=True
for char in s:
    if char<"0" or char>"9":
        flag=False 
        break 
print(flag)

#
s="12345"
flag=True 
i=0 
while i<len(s):
    if s[i]<"0" or s[i]>"9":
        flag=False 
        break 
    i+=1
print(flag)




