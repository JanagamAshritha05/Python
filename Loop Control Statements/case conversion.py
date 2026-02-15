s=input() 
new=""
for i in s[1:]:
    if i.isupper():
        new+="-"+i.lower() 
    else:
        new+=i 
print(s[0].lower()+new) 

#second solution 
s=input() 
len_s=len(s)
first_lower_case=s[0].lower() 
result_string=first_lower_case
for i in range(1,len_s):
    if s[i].isupper(): 
        lower_case_char=s[i].lower() 
        result_string+="-"+lower_case_char 
    else:
        result_string+=s[i]
print(result_string)

# TitleCase  // title-case


