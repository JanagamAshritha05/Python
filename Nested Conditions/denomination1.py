#write a program that reads an amount A and print the min number of 5 and 1 rupee notes required for the given amount.
n=int(input())
a=n//5
b=n%5
print(str(5)+":"+str(a))
print(str(1)+":"+str(b))



