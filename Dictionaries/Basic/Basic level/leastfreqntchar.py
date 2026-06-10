s = 'programming' 

freq = {}

min_val = float("inf")

for char in s:
    count = s.count(char) 

    if count < min_val:
        min_val = count 
        res = char 

print(res)

#
s = "programming"
 
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1 

min_val = min(freq.values()) 

for char in s:
    if freq[char] == min_val:
        print(char)
        break 



