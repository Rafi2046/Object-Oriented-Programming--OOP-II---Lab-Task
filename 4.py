#Python program to solve quadratic equation

import cmath

a = float(input("Enter your number a: "))
b = float(input("Enter your number b: "))
c = float(input("Enter your number c: "))

# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   

