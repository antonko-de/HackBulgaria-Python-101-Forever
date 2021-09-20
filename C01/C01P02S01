def sum_of_digits(n):
    dig_sum = 0
    n = abs(n)
    # initiate a variable that will store the sum of the digits # 
    n_str = str(n)
    # turn the number into a string so we can iterate through it #
    for num in n_str:
        # iterate throught the digits #
        dig_sum += int(num)
        # turn the digit into an int and add it to the sum of all #
    return(dig_sum)






tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1),
]

for test, expected in tests:
    print(test)
    print(expected == sum_of_digits(test))