def turn_into_int_list(side):
    #def a function that makes a list of ints#

    int_list = []
    
    for i in side:
        int_list.append(int(i))

    return int_list


def is_number_balanced(number):
    
    number_as_string = str(number)
    length = len(number_as_string)
    #transform the number into a string #
    
    if length == 1:
        return True
    #cornercase where the number has 1 digit #
    
    split_index = int(length / 2) 
    #get the middle index by deviding the len / 2 and substracting 1 #
    
    if length % 2 == 0:
        left_side = number_as_string[: split_index]
        right_side = number_as_string[split_index :]
        # takes care of the case where the number is even #
    else:
        left_side = number_as_string[: split_index]
        right_side = number_as_string[split_index + 1:]
        # takes care of the case where the number is odd # 



    left_list = turn_into_int_list(left_side)
    #make a list of ints with the left part#
    right_list  =turn_into_int_list(right_side)
    #make a list of ints with the right part#

    return sum(left_list) == sum(right_list)



tests = [
    (9, True),
    (4518, True),
    (28471, False),
    (1238033, True),
    (123, False),
    (11111, True)
]

for test, expected in tests:
    print(test)
    print(expected == is_number_balanced(test))