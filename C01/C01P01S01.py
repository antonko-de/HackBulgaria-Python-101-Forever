

def iban_formatter(iban):
    str_list = []
    iban_form = iban.replace(" ", '')
    #make the format is universal by using join on the input#
    start_index = 0
    for i in range(len(iban_form)):
        if i % 4 == 0 and not i == 0:
            # with a for cycle and an if statement divide the sting into#
            #sub strings#
            str_list.append(iban_form[start_index: i ])
            start_index = i
            #replace the start of the new substring with the last ending#
    str_list.append(iban_form[-2] + iban_form [-1])
    #add the remaining characters#
    return(' '.join(str_list))
    #return the newly created string in the required formatting#

tests = [
    ("BG80BNBG96611020345678","BG80 BNBG 9661 1020 3456 78"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
]

for test, expected in tests:
    print(test)
    print(expected == iban_formatter(test))