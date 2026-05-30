
'''
Rotate D times 
i/p:                o/p:  [3, 4, 5, 1, 2]
[1, 2, 3, 4, 5]
2

i/p:                    o/p: [3, 5, 7, 9, 11, 1]
[1, 3, 5, 7, 9, 11]
25

'''

s = [1, 2, 3, 4, 5]
n = 2

rotations = n%len(s)
start_index = s[:rotations] 
end_index = s[rotations:] 

res = end_index + start_index
print(res)


#
s = [1, 2, 3, 4, 5]
n = 2

rotations = n % len(s)

for i in range(rotations):
    first = s[0]        # save first element
    for j in range(len(s)-1):
        s[j] = s[j+1]  # shift left
    s[-1] = first       # put first at end
print(s)


# 
s=[1, 2, 3, 4, 5]
n = 2

rotations = n%len(s) 
i=0 
while i<rotations:
    first=s[0] 
    j=0 
    while j<len(s)-1:
        s[j]=s[j+1]
        j+=1
    s[-1]=first 
    i+=1 
print(s)



