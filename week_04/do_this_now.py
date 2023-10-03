"""Do this now activities for CP1404 Week 4"""


# from operator import itemgetter

# names = [["Brad", 4], "Kylie", "Joel", "Logan", "Corey"]
#
# try:
#     choice = int(input("Enter number, up to 5: "))
#     print(names[choice-1])
# except ValueError:
#     print("Must enter a number")
# except IndexError:
#     print("Invalid number")

# score_pairs = [["Brad", 4], ["Kylie", 6], ["Joel", 3], ["Logan", 8], ["Corey", 2]]
#
# new_score_pair = input("Enter your name and score (eg Jim 7): ").split()
# new_score_pair[1] = int(new_score_pair[1])
# score_pairs.append(new_score_pair)
# score_pairs.sort(key=itemgetter(1))
# print(score_pairs)

def main():
    """Program for getting a list of tuples containing query string data"""
    url = "https://jcu.edu.au.html?name=Corey&age=34&day=Sat&angry=True"
    pairs = get_query_string_pairs_from_url(url)
    print(pairs)


def get_query_string_pairs_from_url(url):
    """Create a list of query string data tuples from url"""
    pairs = []
    query_string = url[url.find('?') + 1:]
    query_string_categories = query_string.split('&')
    for category in query_string_categories:
        pair = category.split('=')
        try:
            pair[1] = int(pair[1])
        except ValueError:
            pass
        pairs.append(tuple(pair))
    return pairs


main()
