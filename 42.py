# Function to count occurrences of a substring
def count_substring(string, substring):
    return string.count(substring)


main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")


occurrences = count_substring(main_string, sub_string)

print(f"The substring '{sub_string}' occurs {occurrences} times in the main string.")
