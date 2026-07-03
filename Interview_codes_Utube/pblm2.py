# Factorial of number 

n = 5 
prod = 1 
for i in range(1, n+1):
    prod *= i 

print(prod)

# 
def factorial(n):
    if n <= 1:
        return 1 
    return n * factorial(n-1)

n = 5
print(factorial(n))


