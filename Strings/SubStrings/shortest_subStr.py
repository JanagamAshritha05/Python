
s = "ADOBECODEBANC"
t = "ABC"

min_sub = ""

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        
        flag = True
        for char in t:
            if char not in sub:
                flag = False
                break
        
        if flag:
            if min_sub == "" or len(sub) < len(min_sub):
                min_sub = sub

print(min_sub)


#
s = "ADOBECODEBANC"
t = "ABC"

min_sub = ""

i = 0
while i < len(s):
    
    j = i + 1
    while j <= len(s):
        
        sub = s[i:j]
        
        flag = True
        
        k = 0
        while k < len(t):
            if t[k] not in sub:
                flag = False
                break
            k += 1
        
        if flag:
            if min_sub == "" or len(sub) < len(min_sub):
                min_sub = sub
        
        j += 1
    
    i += 1

print(min_sub)


'''
Shortest Substring Containing All Characters
i/p: s = "ADOBECODEBANC"   o/p: BANC
     t = "ABC"

ADOBEC   → contains A,B,C ✔
DOBECODEBA → contains A,B,C ✔
CODEBAN → contains A,B,C ✔
BANC → contains A,B,C ✔ (shortest)

'''



