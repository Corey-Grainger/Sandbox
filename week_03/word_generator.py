"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VALID_FORMAT_CHARACTERS = (VOWELS + CONSONANTS + "%" + "#" + "*")


def main():
    print("Word Formatting: % is a consonant, # is a vowel, * is either, alphabetical characters stay the same")
    word_format = input("Enter word format: ").lower()
    while not is_valid_word_format(VALID_FORMAT_CHARACTERS, word_format):
        print("Invalid word format")
        word_format = input("Enter word format: ").lower()
    word = generate_word_from_word_format(word_format, VOWELS, CONSONANTS)
    print(word)
    word_format_length = int(input("How many letters: "))
    word_format = generate_random_word_format(word_format_length, VALID_FORMAT_CHARACTERS)
    word = generate_word_from_word_format(word_format, VOWELS, CONSONANTS)
    print(word_format)
    print(word)


def generate_word_from_word_format(word_format, vowels, consonants, vowel_wildcard="#", consonant_wildcard="%"):
    word = ""
    for kind in word_format:
        if kind in vowels or kind in consonants:
            word += kind
        elif kind == consonant_wildcard:
            word += random.choice(consonants)
        elif kind == vowel_wildcard:
            word += random.choice(vowels)
        else:
            word += random.choice(vowels+consonants)
    return word


def is_valid_word_format(valid_characters, word_format):
    number_of_invalid_characters = 0
    for character in word_format:
        if character not in valid_characters:
            number_of_invalid_characters += 1
    return number_of_invalid_characters == 0


def generate_random_word_format(word_format_length, valid_characters):
    word_format = ""
    for i in range(word_format_length):
        word_format += random.choice(VALID_FORMAT_CHARACTERS)
    return word_format

main()
