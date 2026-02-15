n=int(input())
k=int(input())
new=[]
for i in range(1,n+1):
    if n%i==0:
        factor=i   
        new.append(i)
new_list=sorted(new,reverse=True)
print(new_list[k-1])

#second approach   
number = int(input()) 
k = int(input())
factor = number
count = 0
kth_factor_found = False
for i in range(1, number+1):
    if not kth_factor_found:
        if (number % factor) == 0:
            count = count + 1
        if count == k:
            print(factor)
            kth_factor_found = True
    factor=factor-1  
    
#12                 #18     
#2      //      6   #4      //  3
