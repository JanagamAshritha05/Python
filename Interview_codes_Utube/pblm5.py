# Nth fibonocci number 

def fibonocci(n):
    a = 0
    b = 1 
    for i in range(n):
        c = a + b 
        a = b 
        b = c 
    return a 

n = 6
print(fibonocci(n))

#
def nth_fibonacci(n):

    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]


n = 6
print(nth_fibonacci(n))

#
def nth_fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return nth_fibonacci(n-1) + nth_fibonacci(n-2)


n = 6
print(nth_fibonacci(n))


