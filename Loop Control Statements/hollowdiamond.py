n=int(input())
for i in range(0,n):
    stars1="* "*(n-i)
    hollow_spaces="  "*(2*i)
    print(stars1+hollow_spaces+stars1)
for i in range(1,n+1):
    stars="* "*i  
    hollow_spaces="  "*(2*(n-i))
    print(stars+hollow_spaces+stars)

#second approach      
n=int(input())
for row in range(0, n): # Upper Hollow Diamond
    stars_count = n - row
    left_stars = "* " * stars_count
    hollow_spaces = "  " * (2*row)
    right_stars = "* " * stars_count
    print(left_stars + hollow_spaces + right_stars)
for row in range(1, n+1): # Lower Hollow Diamond
    stars_count = n - row
    left_stars = "* " * row
    hollow_spaces = "  " * (2 * stars_count)
    right_stars = "* " * row
    print(left_stars + hollow_spaces + right_stars)
 
 
 
 
 
 
    