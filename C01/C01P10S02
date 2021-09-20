def is_palindrome(n):
    reversed = str(n)[::-1]
    # convert the int to str and reverse the str #
    if n == int(reversed):
    #create a conditional check if the number is palindrome #
        return True

def build_cache():
    # we create a cache for a faster algorithm #
    cache_dict = {}
    for number in range(10, 99999 + 1):
        if is_palindrome(number):
            cache_dict[number] = True
            # we include only the palindromes #
    return cache_dict

CACHE = build_cache()

def palindrome_count(n):
    counter = 0
    # initiate a counter variable at 0 #
    for number in range(10, n + 1):
        # creater a for loop in range (10, n) #
        if number in CACHE:
            # check if the number is in the CACHE dict #
            counter += 1
            # if it is increase the counter + 1 #

    return counter
    # return the counter #



tests = [
    (10, 0),
    (20, 1),
    (101, 10),
    (92009, 1009),
    (99999, 1089),
]

for test, expected in tests:
    print(test)
    print(expected == palindrome_count(test))