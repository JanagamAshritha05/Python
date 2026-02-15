sen=input()
new_sen=sen.replace(" ","")
vowels="aeiouAEIOU"
vow=0
con=0
for char in new_sen:
    if char in vowels:
        vow+=1  
    elif char not in vowels:
        con+=1  
print(vow)
print(con)

#print vowels andd consonants 
