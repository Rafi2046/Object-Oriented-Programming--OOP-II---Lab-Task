# Python Program to Convert Decimal to Binary, Octal and Hexadecimal


def convert_number(decimal):
    binary = bin(decimal)   # Convert to binary
    octal = oct(decimal)     # Convert to octal
    hexadecimal = hex(decimal)  # Convert to hexadecimal
    
    return binary, octal, hexadecimal

decimal_number = int(input("Enter a decimal number: "))

binary, octal, hexadecimal = convert_number(decimal_number)

print(f"Decimal: {decimal_number}")
print(f"Binary: {binary[2:]}") 
print(f"Octal: {octal[2:]}")    
print(f"Hexadecimal: {hexadecimal[2:].upper()}") 
