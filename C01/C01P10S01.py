def palindrome_count(n):
    counter = 0
    # initiate a counter variable at 0 #
    for number in range(10, n + 1):
        # creater a for loop in range (10, n) #
        reversed = str(number)[::-1]
        # for each iteration convert the int t str and reverse the str #
        if number == int(reversed):
            # create a conditional check if the number is palindrome #
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
