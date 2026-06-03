#Count Occurrences 

lst = [1, 2, 2, 3, 2, 4]
print(lst.count(2)) 

#
lst = [1, 2, 2, 3, 2, 4]
count = 0
for i in lst:
    if i == 2:
        count += 1
print(count)

#
lst = [1, 2, 2, 3, 2, 4]
print(sum(1 for x in lst if x == 2))


