#print hello world
print("hello world")
# Input and Output
a="gokul"
b=(12)
c= (12.4)
print(a)
print(b)
print(c)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name} and your age is {age}")
# Simple Calculator
number1=int(input("ENTER FIRST NUMBER:"))
number2=int(input("ENTER SECOND NUMBER :"))
add= number1+number2;
sub=number1-number2;
div=number1/number2;
multiply=number1*number2;
print("\nWhat operation would you like to calculate?")
print("1: Addition")
print("2: Subtraction")
print("3: Division")
print("4: Multiplication")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    print(f"The result of addition is: {add}")
elif choice == 2:
    print(f"The result of subtraction is: {sub}")
elif choice == 3:
    print(f"The result of division is: {div}")
elif choice == 4:
    print(f"The result of multiplication is: {multiply}")
else:
    print("Invalid choice! Please select a valid option.")
#odd or even
value=int(input("enter the number:"))
if value%2==0:
    print("even")
else :
    print("odd")


