def char_historgram(string):
    histogram = {}
    # initiate a empy dictionary for later use #
    for i in string:
        # loop over 
        histogram[i] = string.count(i)
        # create a key with each char and use the string count method to #
        # get occurencies#

    return histogram




tests = [
    ('', {}),
    ("    ",{" " : 4}),
    ("Python!",{'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}),
    ("AAAAaaa!!!", {'A': 4, 'a': 3, '!': 3}),
    ("Some very long string here with different casing", {'S': 1,
    'o': 2,
    'm': 1,
    'e': 6,
    ' ': 7,
    'v': 1,
    'r': 4,
    'y': 1,
    'l': 1,
    'n': 4,
    'g': 3,
    's': 2,
    't': 3,
    'i': 4,
    'h': 2,
    'w': 1,
    'd': 1,
    'f': 2,
    'c': 1,
    'a': 1})
    ]

for test, expected in tests:
    print(test)
    print(expected == char_historgram(test))