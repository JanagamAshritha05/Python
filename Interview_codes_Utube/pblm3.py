# How to generate a number in python?

# It Gives random float number between 0 and 1
import random 
num = random.random() 
print(num)

# Gives a random float number in specified range 

num = random.uniform(1, 100)
print(num)

# Random Integer 
num = random.randint(1, 100)
print(num)

# Random Even Number 

num = random.randrange(0, 100, 2)
print(num)

# Random Series 

num = random.sample(range(1, 100), 3)
print(num)


