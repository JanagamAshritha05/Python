
s="aaabbc"
new=""
for char in s:
    if char not in new:
        new+=char 
res=""
for char in new:
    count=s.count(char)
    res+=char+str(count)

print(res)

#
s="aaabbc"
freq={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1 
new=""
for item, val in freq.items():
    new+=item+str(val)
print(new)

#
s = "aaabbc"
freq = {}

# Step 1 - count frequency
i = 0
while i < len(s):
    if s[i] in freq:
        freq[s[i]] += 1
    else:
        freq[s[i]] = 1
    i += 1

# Step 2 - build result
res = ""
for char, count in freq.items():
    res += char + str(count)

print(res)


'''
String Compression

Input: aaabbc
Output: a3b2c1

'''

