#write a program that prints an amount A, and prints the min number of 500, 50, 10 and 1 rupee notes required for the given amount.
M=int(input())
note_500=0  
note_50=0  
note_10=0  
note_1=0  
if M>=500:
    note_500=int(M/500)
    M=int(M%500)
if M>=50:
    note_50=int(M/50)
    M=int(M%50)
if M>=10:
    note_10=int(M/10)
    M=int(M%10)
if M>=1:
    note_1=int(M)
    M=int(M)
print("500: "+str(note_500) + " 50: "+str(note_50) + " 10: "+str(note_10) + " 1: "+str(note_1))
