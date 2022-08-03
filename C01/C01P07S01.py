from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3
# involve the num class because we have a finite amount ot result answers #

def increasing_or_decreasing(ns):
    if len(ns) <= 1:
        return  Monotonicity.NONE
    # deal with the cornercase where you have 0 or 1 integers #
    increases = True
    decreases = True

    for index in range(len(ns) - 1):
        x = ns[index]
        y = ns[index + 1]
        # check what is the Monotonicity with a for loop and a boolean chain #
        increases = increases and  x < y
        decreases = decreases and x > y

    if increases:
        return Monotonicity.INCREASING
        # return the increasing result # 
    if decreases:
        return Monotonicity.DECREASING
        # return the decreasing result #
    return Monotonicity.NONE
    # return the no monotonicty result #






tests = [
    ([1, 2, 3, 4, 5], Monotonicity.INCREASING),
    ([5, 6, -10], Monotonicity.NONE),
    ([1, 1, 1, 1], Monotonicity.NONE),
    ([9, 8, 7, 6], Monotonicity.DECREASING),
    ([], Monotonicity.NONE),
    ([1], Monotonicity.NONE),
    ([1, 100], Monotonicity.INCREASING),
    ([1, 100, 100], Monotonicity.NONE),
    ([100, 1], Monotonicity.DECREASING),
    ([100, 1, 1], Monotonicity.NONE),
    ([100, 1, 2], Monotonicity.NONE)
]

for test, expected in tests:
    print(test)
    print(expected == increasing_or_decreasing(test))