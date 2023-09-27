"""Week 3 do this now activities"""

# filename = input("Enter filename (e.g. lines.txt): ")
# in_file = open("README.MD", "r")
# for line in in_file:
#     if line[0] == "#":
#         print(line.strip("#").strip())
# in_file.close()


# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(name, file=out_file)



# filename = input("Enter filename (e.g. lines.txt): ")
# in_file = open(filename, "r")
# lines = in_file.readlines()
# for line in lines:
#     if line[0] == "#":
#         print(line.strip('#').strip())
# in_file.close()


# with open("guitars.txt") as in_file:
#     in_file.readline()
#     for line in in_file:
#         contents = line.strip().split(",")
#         guitar = contents[0]
#         year = contents[1]
#         price = float(contents[2])
#         print(f"The {guitar} was manufactured in {year} and costs ${price:.2f}")
#
# strings = ["Bob", "Tim", "Jim", "Rob"]
# # for i, string in enumerate(strings, 1):
# #     out_file = open(f"{string}.txt", "w")
# #     print(i, f"{string}", file=out_file, sep=". ")
# #     out_file.close()
#
# for string in strings:
#     try:
#         with open(f"{string}.txt", "r") as out_file:
#             print(string)
#     except FileNotFoundError:
#         print(f"{string}.txt not found")
#

value = int(input("> "))
result = f"{value}" * value
thing = result[value]


