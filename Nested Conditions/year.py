N=input() #write a program to convert N no. of days to years weeks and days.
N=int(N)
years=N//365 
print(years)
weeks=N%365 
res=(weeks//7)
print(res)
days=res%7
print(N-years*365-res*7)

#second Answer
N=input()
N=int(N)
years=N/365
years=int(years)
rem_days=N-(years)*365
weeks=int(rem_days/7)
days=rem_days-(weeks)*7
print(years)
print(weeks)
print(days)



