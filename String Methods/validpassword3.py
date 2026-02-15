password=input()
contains_digit=False
contains_upper=False  
contains_lower=False
for char in password:
    if char.isdigit():
        contains_digit=True   
    elif char.isupper():
        contains_upper=True  
    elif char.islower():
        contains_lower=True  
if contains_digit and contains_upper and contains_lower:
    print("Valid Password")
else:
    print("Invalid Password")
  
#second approach  
password=input() 
contains_digit=False  
for char in password:
    is_digit=char.isdigit()
    if is_digit:
        contains_digit=True   
is_all_upper=(password.upper()==password)
is_all_lower=(password.lower()==password)
if (not is_all_upper and not is_all_lower) and contains_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    
# print valid password if it contains atleast one uppercase, lowercase and digit 

    
    
