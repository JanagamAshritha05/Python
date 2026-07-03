# Print first 10 fibonocci numbers
n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c


# 
n = 10 
a = 0 
b = 1 
for i in range(10):
    print(a, end = " ")
    a, b = b, a + b 

#
n = 10 
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])

for num in fib:
    print(num, end = " ")

    



