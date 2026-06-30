m=int(input())
n=int(input())
  
for i in range(1,m+1):
    if m%i==0 and n%i==0:
        gcd=i  
print(gcd)
#4      //  2   #16     //  1
#6              #9


'''
gcd - greatest common divisor of two or more no's or we can say greatest common factor
or highest common factor(HCF)

ex: gcd(12, 18)

factors of 12 = 1, 2, 3, 4, 6, 12
factors of 18 = 1, 2, 3, 6, 9, 18

common factors = 1, 2, 3, 6
gcd = 6 

'''