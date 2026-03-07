n=4
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
    
for i in range(1, n+1):
    row=""
    for j in range(n-i+1):
        row+=chr(order+j)+" " 
    
    right=""
    for j in range(n-i, -1, -1):
        right+=chr(order+j)+" "
    print(row + "  "*(2*i-2) + right)
  
  
# 
n=4
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
    
i=1 
while i<=n:
    row=""
    j=0
    while j<n-i:
        row+=chr(order+j)+" " 
        j+=1 
    
    right=""
    j=n-i-1
    while j>=0:
        right+=chr(order+j)+" "
        j-=1 
    print(row + "  "*(2*i) + right)
    i+=1  
    
    
    


