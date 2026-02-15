n = int(input())
number_of_pairs = 0
for num in range(1, n):
    if n - num < n  and num < n - num:
        number_of_pairs = number_of_pairs + 1
print(number_of_pairs)

