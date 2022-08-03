

def group(items):
    lenght = len(items)
    # assign the len of the list to a variable for multiple later use #
    index = 0
    # create a variable for later while loop control #
    grouped_list = []
    # initiate the outer list instance #
    digit_group = []
    # initiate the inner list instance #

    while index < lenght:
        # outer for loop which will give us the start of patterns #
        digit = items[index]
        # get the first digit of each new pattern # 
        look_ahead = index + 1
        # get a variable for which too look in the indexes ahead #
        digit_group = [digit]
        # put value in the inner list for start of a pattern #
        while look_ahead < lenght and items[look_ahead] == digit:
            # while loop which will gives us the volume of the patterns #
            digit_group.append(items[look_ahead])
            look_ahead += 1

        grouped_list.append(digit_group)
        # attack each inner list to the outer list #
        index = look_ahead

    return grouped_list










tests = [
    ([1, 1, 1, 2, 3, 1, 1],[[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3],[[1], [2], [1], [2], [3, 3]]),
    ([],[]),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]])
]

for test, expected in tests:
    print(test)
    print(group(test))
    print(expected == group(test))