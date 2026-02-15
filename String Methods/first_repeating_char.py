s = "abcaebd"
seen = set()

for char in s:
    if char in seen:
        print("First repeating character:", char)
        break
    seen.add(char)

