#write a program that prints an amount A, and prints the min number of 5000,500,200,50,20,5,2 and 1 rupee notes required for the given amount.

M=int(input())
note_2000=0  
note_500=0  
note_200=0 
note_50=0 
note_20=0  
note_5=0  
note_2=0  
note_1=0  

if M>=2000:
    note_2000=int(M/2000)
    M=(M%2000)
if M>=500:
    note_500=int(M/500)
    M=(M%500)
if M>=200:
    note_200=int(M/200)
    M=(M%200)
if M>=50:
    note_50=int(M/50)
    M=(M%50)
if M>=20:
    note_20=int(M/20)
    M=(M%20)
if M>=5:
    note_5=int(M/5)
    M=(M%5)
if M>=2:
    note_2=int(M/2)
    M=(M%2)
if M>=1:
    note_1=int(M)
    M=(M)
print("2000:"+str(note_2000) + " 500:"+str(note_500) + " 200:"+str(note_200) + " 50:"+str(note_50) + " 20:"+str(note_20) + " 5:"+str(note_5) + " 2:"+str(note_2) + " 1:"+str(note_1))


