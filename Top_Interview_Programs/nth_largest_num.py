l = [10, 45, 3, 99, 23]
n = 2

for i in range(n):
    max_num=l[0] 
    for num in l:
        if num>max_num:
            max_num=num 
    l.remove(max_num)

print(max_num)




