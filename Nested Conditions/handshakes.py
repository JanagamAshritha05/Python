#It was Raj's first day at school.His teacher Anu asked the students to meet every other student in the 
#class and introduce themselves.The teacher asked them to do handshakes when they meet each other.
#Write a program that reads an integer N and prints the number of handshakes made by the students.
#i/p: 5 o/p: 10 i/p: 3  o/p: 3
n=int(input())
first_person_shakes_hand=0
second_person_shakes_hand=0 
third_person_shakes_hand=0 
fourth_person_shakes_hand=0 
nth_person=(n-1)
handshakes=0

if first_person_shakes_hand==n-1:
    handshakes=(n-1)
if second_person_shakes_hand==n-2:
    handshakes=(n-1)+(n-2)  
if third_person_shakes_hand==n-3:
    handshakes=(n-1)+(n-2)+(n-3)
if fourth_person_shakes_hand==n-4:
    handshakes=(n-1)+(n-2)+(n-3)+(n-4)
if nth_person==n-1:
    handshakes=int((n-1)*(n)/2) 
print(handshakes)

#second solution
def ans(n):
    return n*(n-1)//2
    
n=int(input()) 
print(ans(n))



    