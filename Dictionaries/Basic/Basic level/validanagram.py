'''
Two strings are anagrams if they contain the same characters with
the same frequencies, but the order can be different.

'''
s1 = "listen"
s2 = "silent" 

if len(s1) != len(s2):
    print(False) 

else:
    freq = {}

    for i in range(len(s1)):
        freq[s1[i]] = freq.get(s1[i], 0) + 1 
        freq[s2[i]] = freq.get(s2[i], 0) - 1 

print(all(value == 0 for value in freq.values())) 



