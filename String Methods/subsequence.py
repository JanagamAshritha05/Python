s1 = "abc"
s2 = "aebdc"

index = 0
for char in s2:
    if index < len(s1) and char == s1[index]:
        index += 1

if index == len(s1):
    print(f"Yes, {s1} is a subsequence of {s2}")
else:
    print(f"No, {s1} is not a subsequence of {s2}")



