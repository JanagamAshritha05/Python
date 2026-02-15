n=int(input())      # "1"+"11"+"111"=246
term="2"
sum=0
for i in range(1,n+1):
    term_number=int(term*i)
    sum+=term_number   
print(sum)


