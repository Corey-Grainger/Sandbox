#
# """
# Produce the following sorted and formatted output
# Bob         = 612
# Xavier      =  80
# Chantanelle =   9
# Derek       =   7
# """
#
# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# # Now, what if this were a dictionary?
# from operator import itemgetter
# name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# name_score_pairs = list(name_to_score.items())
# name_score_pairs.sort(key=itemgetter(1), reverse=True)
# longest_name = max((len(name_score_pair[0]) for name_score_pair in name_score_pairs))
# name_to_score = dict(name_score_pairs)
# for name, score in name_to_score.items():
#     print(f"{name:{longest_name}} = {score:3}")

#
# STRINGS = ["Blah Blah", "Hello World", "Goodbye", "CP1404"]
#
#
# def generate_string_to_length_of_string(strings):
#     """Generate a dictionary of string to length of string from a list of strings"""
#     string_to_length_of_string = {}
#     for string in strings:
#         string_to_length_of_string[string] = len(string)
#     return string_to_length_of_string
#
#
# def test_function():
#     string_to_length_of_string = generate_string_to_length_of_string(STRINGS)
#     print(string_to_length_of_string)
#
#
# test_function()

{}



