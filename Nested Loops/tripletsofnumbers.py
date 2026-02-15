n = int(input())

number_of_pairs = 0
for first_number in range(1, n):
    for second_number in range(first_number + 1, n):
        if n - (first_number + second_number) < n and first_number < second_number < n - (first_number + second_number):
            number_of_pairs = number_of_pairs + 1 
print(number_of_pairs)
