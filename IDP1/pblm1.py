'''
Arjun has two strings:

S
T

He is allowed to:

Select any two adjacent characters in S

Swap them

Perform this operation only once

After the swap, check whether S becomes equal to T.

If yes → print "Yes"

Otherwise → print "No"

For example:

abcde

Adjacent pairs are:

a b
b c
c d
d e

Indices:

0 1
1 2
2 3
3 4

You can swap only these pairs.

'''

s = "abc"
t = "acb" 

if s == t:
    print("Yes")

else:
    
    for i in range(len(s)-1):
        temp =list(s)

        temp[i], temp[i+1] = temp[i+1], temp[i] 

        if ''.join(temp) == t:
            print("Yes") 
            break 

    else:
        print("No")

# 
s = input()
t = input()

if s == t:
    print("Yes")

else:
    for i in range(len(s)-1):

        if s[i] != t[i]:

            if (s[i] == t[i+1] and
                s[i+1] == t[i] and
                s[i+2:] == t[i+2:]):

                print("Yes")
            else:
                print("No")

            break
    else:
        print("No")
        
        
        










