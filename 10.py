# Python Program to check if a Number is Positive, Negative or Zero

def number_check(a):
    if a>0:
        print("Your Number Is Positive")
    elif a<0:
        print("Your Number is Negative")
    else:
        print("Your Number is 0")
a= float(input("Enter Your Number: "))        
number_check(a)