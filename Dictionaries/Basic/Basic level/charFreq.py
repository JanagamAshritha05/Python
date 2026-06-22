
s = "programming"

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

print(freq)  # Repeating characters not appears multiple times because keys must always be unique.


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

'''
If character exists → take its count and add 1
If character does not exist → start with 0 and add 1

'p' not in dict → 0 + 1 = 1 → {'p': 1}

'r' appears again → 1 + 1 = 2 → {'r': 2}
'''





