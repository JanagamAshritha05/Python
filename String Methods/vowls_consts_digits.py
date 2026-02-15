
s = "Python@123"
v = 0
c = 0
d = 0
sp = 0  # renamed special char counter

for char in s:
    if char in "aeiouAEIOU":
        v += 1
    elif char.isalpha():
        c += 1
    elif char.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)
