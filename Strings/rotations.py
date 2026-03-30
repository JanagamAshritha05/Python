
s1="abcde"
s2="deabc"

if len(s1)==len(s2) and s2 in (s1+s1):
    print("True")
else:
    print("False")


#
s1 = "abcde"
s2 = "cdeab"

flag = False

for i in range(len(s1)):
    rotated = s1[i:] + s1[:i]
    if rotated == s2:
        flag = True
        break

print(flag)


#
s1 = "abcde"
s2 = "cdeab"

flag=False
i=0 
while i<len(s1):
    rotated = s1[i:] + s1[:i]
    if rotated == s2:
        flag=True 
        break 
    i+=1 
    
print(flag)




