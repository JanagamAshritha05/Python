# Print Armstrong Numbers in a Range 

m = 1 
n = 1000 

new = []

for i in range(m, n+1):
    sum = 0 
    for j in str(i):
        sum += int(j)**len(str(i)) 

    if sum == i:
        new.append(i) 

if len(new)>1:
    print(new)
else:
    print("Not an Arrmstrong Numbers")


# 
start = 1
end = 1000

for n in range(start, end + 1):
    digits = len(str(n))
    total = sum(int(d) ** digits for d in str(n))

    if total == n:
        print(n, end=" ") 





