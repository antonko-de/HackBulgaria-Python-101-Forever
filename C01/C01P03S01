from math import factorial
# import the math module so we can use the factorial method

def fact_digits(n):
    n = str(n)
    # convert the integer into a string so we can iterate through it
    factorials = []
    # initiate a list for later use 
    for i in n:
        factorials.append(factorial(int(i)))
        # iterate throught the digits and use the factorial method
    return sum(factorials)




tests = [
    (101,3),
    (111,3),
    (145,145),
    (999, 1088640),
]

for test, expected in tests:
    print(test)
    print(expected == fact_digits(test))