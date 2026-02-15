 #write a program to calculate the electricity bill for a household consumed. The price for unit varies based in the slab.charges per unit for 
 #different slabs are as 
 #for the first 50 units (0-50), the charge is 2/unit.
 #for the next 100 units (51-150), the charge is 3/unit.
 #for the next 100 units (151-250), the charge is 5/unit.
 #for 250 and above , the charge is 8/unit  
 # additional surcharge of 20% added on the total amount is added to the bill.

units=int(input())
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

    
    