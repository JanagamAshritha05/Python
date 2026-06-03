'''
Unzip List 
Input:  [(1,'a'), (2,'b'), (3,'c')]
Output:
Numbers : [1, 2, 3]
Letters : ['a', 'b', 'c']

'''
lst = [(1,'a'), (2,'b'), (3,'c')] 

nums = []
letters = []

for num, char in lst:
    nums.append(num)
    letters.append(char) 
print(nums)
print(letters)

#
lst = [(1,'a'), (2,'b'), (3,'c')]

numbers, letters = zip(*lst)

print("Numbers :", list(numbers))
print("Letters :", list(letters))  

#
lst = [(1,'a'), (2,'b'), (3,'c')]

numbers = []
letters = []

i = 0

while i < len(lst):
    numbers.append(lst[i][0])
    letters.append(lst[i][1])
    i += 1

print("Numbers :", numbers)
print("Letters :", letters)

#
lst = [(1,'a'), (2,'b'), (3,'c')]

numbers = [item[0] for item in lst]
letters = [item[1] for item in lst]

print("Numbers :", numbers)
print("Letters :", letters)



