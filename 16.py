# Python Program to Display the Multiplication Table

num = int(input("Enter Your Number For Your Multiplication Table : "))
print("The Multiplication Table of :",num)
for count in range(1,11):
    print(num,'x',count,'=',num*count)