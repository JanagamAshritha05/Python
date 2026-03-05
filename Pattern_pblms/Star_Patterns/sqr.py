
n=4 

for i in range(n):
    print("* "*n)


#
n = 4

for i in range(n):
    new=""
    for j in range(n):
        new+="* " 
    print(new)
    

#
n=4 

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 

n=4 

i=0
while i<n:
    j=0 
    while j<n:
        print("*", end=" ")
        j+=1 
    print()
    i+=1 





# By default, print() moves the cursor to the next line after printing
# The 'end' parameter changes this default behavior
# If end=" ", print() will NOT go to the next line
# Instead, it will print a space after the output
# This is why 'end' is used in patterns to print on the same line
# To move to the next line again, we use an empty print()

