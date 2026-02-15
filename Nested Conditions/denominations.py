#Ex: i/p:8593 
#o/p: 1000:8
#     500:1
#     100:0
#     50:1
#     20:2
#     5:0
#     1:3

N=int(input())
note_1000=0 
note_500=0 
note_100=0 
note_50=0 
note_20=0 
note_5=0 
note_1=0 
if N>=1000:
    note_1000=int(N/1000)
    N=(N%1000)
if N>=500:
    note_500=int(N/500)
    N=(N%500) 
if N>=100:
    note_100=int(N/100)
    N=(N%100) 
if N>=50:
    note_50=int(N/50)
    N=(N%50) 
if N>=20:
    note_20=int(N/20)
    N=(N%20) 
if N>=5:
    note_5=int(N/5)
    N=(N%5)
if N>=1:
    note_1=int(N/1)
    N=N%1
print("1000:"+str(note_1000))
print("500:"+str(note_500))
print("100:"+str(note_100))
print("50:"+str(note_50))
print("20:"+str(note_20))
print("5:"+str(note_5))
print("1:"+str(note_1))


