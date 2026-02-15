word=input()
green_count=0  
red_count=0
for i in range(len(word)):
    if word[i]=="G":
        green_count+=1  
    else:
        red_count+=1  
if green_count<red_count:
    print(green_count)
else:
    print(red_count)
    
#second approach
N=input()
red=N.count('R')
green=N.count('G')
if red>green:
    count=green   
else:
    count=red
print(count)

#we make sure that all the colors same 
#i/p:   GGGGGR  o/p: 1
#we have to change one color R to get all the same