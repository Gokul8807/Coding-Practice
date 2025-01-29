year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Leap year: {year}")
else:
    print("Not a leap year")
