def anagrams(word1, word2):
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')
    # take the two strings and remove the whitespace #
    word1 = word1.lower()
    word2 = word2.lower()
    # take the two strings and ensure they are lowercase #
    word1 = list(word1)
    word2 = list(word2)
    # splits the strings into lists #
    word1.sort()
    word2.sort()
    # sort the lists # 
    return word1 == word2
    # get the result from the comparison #



tests = [
    ("listen", "silent", True),
    ("LISTEN", "silent", True),
    ("python", "ruby", False),
    ("New York Times", "monkeys write", True),
    ("snake", "sssnakee", False),
]

for test, test1, expected in tests:
    print(test)
    print(expected == anagrams(test, test1))