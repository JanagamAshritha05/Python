n=int(input())
for i in range(65,65+n):
    char=""
    for j in range(65,i+1):
        char+=chr(j)+" "
    print(char)
    
#second solution  
N=int(input())
for row in range(1,N+1):
    new_letter=""
    for letter in range(65,65+row):
        new_letter+=chr(letter)+" "
    print(new_letter)
    
