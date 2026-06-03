# List Length

lst = [10, 20, 30, 40, 50]
print(len(lst))

#
lst = [10, 20, 30, 40, 50]
count = 0
for i in lst:
    count += 1
print(count)

#
lst = [10, 20, 30, 40, 50]
length = sum(1 for _ in lst)
print(length)


