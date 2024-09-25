# Python Program to Print Reverse of a String
def reverse_string(s):
    return s[::-1]


string = input("Enter a string: ")


reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
