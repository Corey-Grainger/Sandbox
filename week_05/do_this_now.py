#
# NAMES = ["Abe", "Homer", "Marge", "Lisa", "Bart", "Maggie", "Mona"]
# AGES = [80, 84, 89, 8, 10, 2, 80]




# def main():
#     """Display the oldest person in parallel lists of names and ages"""
#     oldest_person = determine_oldest_person_in_parallel_lists(NAMES, AGES)
#     print(oldest_person)
#
#
# def determine_oldest_person_in_parallel_lists(names, ages):
#     """Return the name of the oldest person in parallel lists of names and ages."""
#     return names[ages.index(max(ages))]
# main()


# name_to_age = {"Bill": 21, "Jane": 4, "Sven": 56}
#
# name = input("Name: ")
# is_valid_age = False
# while not is_valid_age:
#     try:
#         age = int(input("Age: "))
#         while age < 0:
#             print("Age must be > 0")
#             age = int(input("Age: "))
#         is_valid_age = True
#     except ValueError:
#         print("Invalid age")
# name_to_age[name] = age # Error checking ensures age is defined
# for name, age in name_to_age.items():
#     print(f"{name:20} -    {age:3}")
