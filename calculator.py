print("welcome to tip calculator")
bill=int(input("what was total bill?$"))
tip=int(input("what % tip would you give? 10 20 40"))
people=int(input("how many people to split the bill?"))
tip_as_percentage=tip/100
total_tip_amount=bill*tip_as_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_bill=(round(bill_per_person))
print(f"each  person should pay{final_bill}$")
           
