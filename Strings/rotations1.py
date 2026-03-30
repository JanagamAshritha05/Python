
'''
Write a program that reads two words s1 and s2 and check if s2 is rotation of s1 or not 
otherwise print No Match

i/P:        o/p: 2    i/p:  python  o/p: 0 
python                      python 
onpyth  

'''

s1="python"
s2="onpyth"

for i in range(len(s1)):
    res = s1[-i:] + s1[:-i]
    if res == s2:
       print(i)
       break 
else:
    print("No match")


# 
s1="python"
s2="python"
i=0 
while i<len(s1):
    res=s1[-i:] + s1[:-i]
    if res==s2:
        print(i)
        break 
    else:
        print("No Match")
    i+=1


#
s1 = "python"
s2 = "onpyth"

for i in range(len(s1)):
    res = s1[i:] + s1[:i]
    if res == s2:
        print(i)
        break
else:
    print("No Match")

    

