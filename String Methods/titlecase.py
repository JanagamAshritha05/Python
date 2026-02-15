string=input() 
spaced=string[0]
for char in string[1:]:
    if char.isupper():
        spaced+=" "+char 
    else:
        spaced+=char 
print(spaced)

#Second Solution 
def add_space_before_uppercase(s):
    spaced = s[0]  # start with the first character
    for c in s[1:]:
        if c.isupper():
            spaced += ' ' + c
        else:
            spaced += c
    print(spaced)

title=input()
add_space_before_uppercase(title)

# ex: TitleCase   o/p: Title Case
