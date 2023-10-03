"""Program to remove a name from a list of names"""


names = ["Ada", "Alan", "Bill", "John"]

print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
        print(f"You removed {name_to_remove}")
    except ValueError:
        print("Name not in names")
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove? ")
