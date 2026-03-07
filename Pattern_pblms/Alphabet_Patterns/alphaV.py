n=5
order = 65

for i in range(1, n+1):
    left = ""
    for j in range(i):
        left += chr(order + j) + " "
        
    right = ""
    for j in range(i - 1, -1, -1):
        right += chr(order + j) + " "

    gap = " " * (2 * (n - i) * 2)

    print(left + gap + right)
    
    
# 
n=5 
order=65 
i=1 
while i<=n:
    row=""
    j=0
    while j<i:
        row+=chr(order+j) + " "
        j+=1 
    
    right=""
    j=i-1
    while j>=0:
        right+=chr(order+j) + " "
        j-=1
    gap=" "*(2*(n-i)*2)
    print(row + gap + right)
    i+=1 
    
    
 