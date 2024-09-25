# Python Program to Sort Words in Alphabetic Order

my_str = input("Enter a string: ")  
 
words = my_str.split()  
 
words.sort()  
 
for word in words:  
   print(word)