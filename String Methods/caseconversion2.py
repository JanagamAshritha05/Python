string=input() 
new=""
for i in string:
    if i.isupper():
        new+="-"+i.lower()
    else:
        new+=i 
print(new) 

#Second Solution 
def add_hyphen_and_lower_case(s):
    hyphenated = ''
    for i, c in enumerate(s):
        if i > 0 and c.isupper():
            hyphenated += '-' + c.lower()
        else:
            hyphenated += c.lower()
    print(hyphenated)

# aChristamastory  o/p:  a-christamas-story 
# theFox   o/p:  the-fox 

