#a=str(input("Enter ths string:"))
#print(a[::-1]) # reversing char by using stringslicing
number =[1,2,4,5]
for i in range(3):
    if (number[i+1] - number[i]!=1): 
        print(number[i]+1)
