string=input()
new_string=string.lower()
reverse=""
for char in new_string:
    reverse=char+reverse   
if reverse==new_string:
    print("Palindrome")
else:
    print("Not a Palindrome")
    