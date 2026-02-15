s1=input() 
s2=input() 
result=""
for i in range(len(s1)):
    if i%2==0:
        result+=s1[i]
    else:
        result+=s2[i]
print(result)

# Given two strings of equal length write a program that prints a new 
# strings by appending characters froms1 first and then from s2 alternately.

# bring     // baieg        APPRECIATE   //    AAPKEAIKTAR
#camel                      BACKPACKER 
