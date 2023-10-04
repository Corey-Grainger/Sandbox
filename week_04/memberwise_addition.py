""""CP1404 Week 04 memberwise addition function prac"""


def main():
    memberwise_numbers = add_memberwise([1, 2, 3], [4, 5, 6])
    print(memberwise_numbers)
    memberwise_numbers = add_memberwise([1, 2, 3], [1, 2, 3, 4])
    print(memberwise_numbers)
    memberwise_numbers = add_memberwise([2, 4, 6, 8], [1, 2, 3])
    print(memberwise_numbers)

def add_memberwise(first_numbers, second_numbers):
    summed_numbers = []
    if first_numbers > second_numbers:
        longest_numbers = first_numbers
        shortest_numbers = second_numbers
    else:
        longest_numbers = second_numbers
        shortest_numbers = first_numbers
    for i, number in enumerate(longest_numbers):
        try:
            number += shortest_numbers[i]
            summed_numbers.append(number)
        except IndexError:
            summed_numbers.append(number)
    return summed_numbers


main()
