def nan_expand(times):
    if times  == 0:
        # make a conditional check for the zero case #
        return('')
    else:
        return(f'{"Not a " * times}NaN')
        # return the required number of repetitions of the string









tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for test, expected in tests:
    print(test)
    print(expected == nan_expand(test))