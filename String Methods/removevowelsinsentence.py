word=input()
vowels="aeiouAEIOU"
new=""
for char in word:
    if char not in vowels:
        new+=char  
print(new)
