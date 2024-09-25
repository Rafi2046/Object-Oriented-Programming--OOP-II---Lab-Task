# Python Program to Calculate the Power of a Number

def power(base, exponent):
    return base ** exponent  

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
