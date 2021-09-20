

def list_transform(number):
    # transforms the number into a list of digits #
    ls_digits = list(str(number))
    digit_list =[int(i) for i in ls_digits]
    return digit_list

def iteration_and_multiplication(digit_list):
    # iterates through every second digit backwards and multiplies it by 2#
    lenght = len(digit_list)
    for index in range(lenght - 2, -1, -2):
        digit_list[index] = digit_list[index] * 2
    return digit_list

def digit_transform(number):
    # we take of the case where the number is no longer single digit#
    # we slice the number into digits and we sum them #
    str_num = str(number)
    return int(str_num[0]) + int(str_num[1])


def under_over_check(digit_list):
    length = len(digit_list)
    # we iterate through the new list and check if any of the items is a double digit num #
    for index in range(0, length):
        if digit_list[index] >= 10:
            digit_list[index] = digit_transform(digit_list[index])
    return digit_list



def is_credit_card_valid(number):
    # we combine our functions into a working Luhm algorithm #
    number_as_list = list_transform(number)
    multiplied_sequence = iteration_and_multiplication(number_as_list)
    transformed_sequence = under_over_check(multiplied_sequence)

    if sum(transformed_sequence) % 10  == 0:
        return True
    else:
        return False




tests = [
    ("79927398713", True),
    ("79927398715", False),
    ("4417123456789113", True),
]

for test, expected in tests:
    print(test)
    print(expected == is_credit_card_valid(test))