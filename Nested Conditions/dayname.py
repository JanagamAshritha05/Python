units=int(input()) # write a program that reads a day number and prints the corresponding day name.
if units<=50:
    units=units*2 
elif units<=150:
    units=(2*50)+(3*(units-50))
elif units<=250:
    units=(2*50)+(3*100)+(5*(units-150))
elif units>=250:
    units=(2*50)+(3*100)+(5*100)+(8*(units-250))
surcharge=0.2*units 
print(surcharge+units)
