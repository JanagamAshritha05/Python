#write a program that prints an amount A, and prints the minimum number pf 100, 50, 10 and 1 rupee notes required for the given number.
number=int(input())
note_100=0  
note_50=0  
note_10=0 
note_1=0 

if number>=100:
    note_100=int(number/100)
    number=(number%100)
if number>=50:
    note_50=int(number/50)
    number=(number%50)
if number>=10:
    note_10=int(number/10)
    number=(number%10)
note_1=number 
print("100:"+str(note_100))
print("50:"+str(note_50))
print("10:"+str(note_10))
print("1:"+str(note_1))


