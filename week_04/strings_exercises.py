"""CP1404 Exercises for lists of strings"""

user_strings = []
user_string = input("Enter string: ")
while user_string != "":
    user_strings.append(user_string)
    user_string = input("Enter string: ")
repeated_strings = [string for string in user_strings if user_strings.count(string) > 1]
if len(repeated_strings) == 0:
    print("No repeated strings entered")
else:
    printed_strings = []
    for string in repeated_strings:
        if string not in printed_strings:
            print(string)
            printed_strings.append(string)

