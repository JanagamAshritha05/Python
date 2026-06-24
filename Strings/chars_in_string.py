s="python"
count=0 

for char in s:
    count+=1 
print(count) 

#
s="python"
count=0 
i=0 
while i<len(s):
    count+=1 
    i+=1 
print(count)

#
s="python"
print(len(s))

#
s="python" 
print(sum(1 for char in s))

# 
s = "python"

def find_len(s):
    if s == "":
        return 0 
    
    return 1 + find_len(s[1:])

print(find_len(s))




