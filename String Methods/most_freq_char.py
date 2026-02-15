s = "programming"
max_freq = 0
freq_chars = []

# First, find the max frequency
for char in s:
    count = s.count(char)
    if count > max_freq:
        max_freq = count

# Then, find all characters with that max frequency
for char in s:
    if s.count(char) == max_freq and char not in freq_chars:
        freq_chars.append(char)

print("Most frequent characters:", ", ".join(freq_chars))





