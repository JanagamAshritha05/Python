a = 12
b = 15

# Step 1: Find the greater number
if a > b:
    greater = a
else:
    greater = b

# Step 2: Keep checking if greater is divisible by both a and b
while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1

print(lcm)

