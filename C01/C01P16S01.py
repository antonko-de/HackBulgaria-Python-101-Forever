def sort_out_clicks(list_of_numbers):
    index = 0
    lenght = len(list_of_numbers)
    grouped_clicks = []
    # we define our starting index, while base case and we initiate a lits we gonna use later #
    # to append all the grouped clicks#
    while index < lenght:
        # use the algorith from a previous exercise where we start to iterate though our list #
        # of clicks with a while loop. We set a item we gonna use for initial comparison #
        # we defince a look ahead index for comparison #
        current_digit = list_of_numbers[index]
        look_ahead = index + 1
        current_group = [current_digit]
        while look_ahead < lenght and current_digit == list_of_numbers[look_ahead]:
            # inner loop thats gonna separte our clicks #
            current_group.append(current_digit)
            look_ahead += 1
        grouped_clicks.append(current_group)
        index = look_ahead
    return grouped_clicks


symbols_dict = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
# a dictionary that imitates the buttons of a retro cell #
def right_length(index, lenght):
    return index < lenght

def numbers_to_message(pressed_sequence):
    sorted_clicks = sort_out_clicks(pressed_sequence)
    word = []
    capital = False
    # we initiate a boolen for the digit 1 case which capitalizes the next letter in our message #
    for item in sorted_clicks:
        button = item[0]
        if button == 1:
            # when we must capitalize next#
            capital = True
            continue
        if button == 0:
            # when we must add an interval to the message #
            word.append(' ')
            continue
        if button == -1:
            # just skip #
            continue
        length = len(symbols_dict[button])
        if not item.count(button) == 1:
            index = (item.count(button) - 1) % length
            # we use modul to ensure we get a symbol even when the clicks exceed the len of the value#
        else:
            index = item.count(button) - 1
            # corner case where the modulo wont work #
        if capital:
            # the case where we must capitalise #
            symbol = symbols_dict[button][index].upper()
            capital = False


        else:
            symbol = symbols_dict[button][index]
        # we append the symbol to the list #
        word.append(symbol)
    # we return the joined message #
    return ''.join(word)

tests = [
   ([2, -1, 2, 2, -1, 2, 2, 2], "abc"),
    ([2, 2, 2, 2], "a"),
    ([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2], "Ivo e Panda")
]

for test, expected in tests:
   print(expected == numbers_to_message(test))






