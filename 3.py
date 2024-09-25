#Python program to find the area of a triangle formula  = (s*(s-a)*(s-b)*(s-c))-1/2

a = float (input('Enter The first side: '))
b = float (input('Enter The Second  side: '))
c = float (input('Enter The Third side: '))

s =(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))-1/2
print('The area of the triangle is %0.2f' %area)   
