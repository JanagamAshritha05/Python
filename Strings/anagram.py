
s1="listen"
s2="silent"

if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
    
# 
s1="listen"
s2="silent"
freq1={}
freq2={}

for char in s1:
    if char in freq1:
        freq1[char]+=1 
    else:
        freq1[char]=1 
        
for char in s2:
    if char in freq2:
        freq2[char]+=1 
    else:
        freq2[char]=1 

if freq1==freq2:
    print("Anagram")
else:
    print("Not an anagram")


# 
s1="listen"
s2="silent"
freq1={}
freq2={}

for char in s1:
    freq1[char]=freq1.get(char, 0)+1 

for char in s2:
    freq2[char]=freq2.get(char, 0)+1 

if freq1==freq2:
    print("Anagram")
else:
    print("Not an Anagram")
    
    
'''
Two strings are Anagram if they contain same characters with same frequency just in different order.
"listen" → jumble letters → "silent" 
Same letters, different order → Anagram!

'''








