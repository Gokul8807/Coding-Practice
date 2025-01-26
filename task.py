number=int(input("enter the number :"))
if number%3==0 and number%4==0:
    print("number + good morning ")
elif number%4==0:
    print("GOOD AFTERNOON")
elif number%3==0:
    print("Good Evening")
else:
    print("good night")
