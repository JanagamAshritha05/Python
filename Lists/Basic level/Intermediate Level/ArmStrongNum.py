'''
An Armstrong number is a number that is equal to the sum 
of its digits raised to the power of the number of digits.

Example 1: 153

Number of digits = 3

 1**3 + 5**3 + 3**3 = 153 

'''

n = 153
len_ = len(str(n))
sum = 0 
for i in str(n):
    sum += int(i)**len_ 

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 
n = 153

digits = len(str(n))

total = sum(int(digit) ** digits for digit in str(n))

print("Armstrong Number" if total == n else "Not Armstrong")


