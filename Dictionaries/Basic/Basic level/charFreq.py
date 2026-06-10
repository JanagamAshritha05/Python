
s = "programming"

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

print(freq) 

#
s = 'programming' 

freq = {} 

for char in s:
    if char in freq:
        freq[char]+=1 
    else:
        freq[char]=1 

print(freq)

#
s = "programming" 

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1 

print(freq)


