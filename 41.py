# Function to swap case of each character in the string
def swap_case(s):
    return s.swapcase()


input_string = input("Enter a string: ")


swapped_string = swap_case(input_string)
print("Swapped case string:", swapped_string)
