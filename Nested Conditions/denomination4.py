#write a program that prints an amount A, and prints the min number of 100, 50, 20 and 10 rupee notes required for the given amount.
A=int(input())
note_100=0 
note_50=0 
note_20=0 
note_10=0  
 
if A>=100:
    note_100=int(A/100)
    A=int(A%100)
if A>=50:
    note_50=int(A/50)
    A=int(A%50)
if A>=20:
    note_20=int(A/20)
    A=int(A%20)
if A>=10:
    note_10=int(A/10)
    A=int(A%10)

print("100 Notes: "+str(note_100))
print("50 Notes: "+str(note_50))
print("20 Notes: "+str(note_20))
print("10 Notes: "+str(note_10))

