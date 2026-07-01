def fibonocci(n):
    if n <= 1:
        return n 
    return fibonocci(n-2) + fibonocci(n-1)

def fibonocci_series(n):
    fibonocci_series = []
    for i in range(n):
        term = fibonocci(i)
        fibonocci_series.append(term)
    return fibonocci_series 

n = 5
res = fibonocci_series(n)
print(res)


