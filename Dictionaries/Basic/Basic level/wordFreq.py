s = "python is easy python is powerful"

words = s.split()
freq = {}

for word in words:
    freq[word] = words.count(word)

print(freq)

#

s = "python is easy python is powerful"

words = s.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)

# 

s = "python is easy python is powerful"

freq = {}

for word in s.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)


