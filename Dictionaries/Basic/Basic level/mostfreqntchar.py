
s = "banana"

freq = {}

max_val = 0 

for char in s:
    count = s.count(char) 

    if count > max_val:
        max_val = count 
        res = char 

print(res)

# 
s = "banana" 

freq = {}

for char in s: 
    freq[char] = freq.get(char, 0) + 1 

max_freq = max(freq.values()) 

for char in s:
    if freq[char] == max_freq:
        print(char) 
        break 



