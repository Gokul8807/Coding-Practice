weight = int(input("Enter the weight of clothes in grams: "))
if weight <= 2000: 
     print("Time Needed: 25 minutes") 
elif 2001 <= weight <= 4000:  
    print("Time Needed: 35 minutes")

elif 4000 <=weight <=7000:
    print("Time Needed: 45 minutes")
else:
    print("Over load")