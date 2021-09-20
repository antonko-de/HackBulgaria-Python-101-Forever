def build_prime_cache(num):
    # to create a cache will all the primes in the range from 2 to the input number#
    # Here I can use mine :D #
    prime_nums = []
    for number in range(2, num + 1):
        prime = True
        for factor in range(2, number):
            if number % factor == 0:
                prime = False   
        if prime:
            prime_nums.append(number)
    return prime_nums


def goldbach(num):
    # iterate over all the items in the CACHE #
    # if we find a pair make sure to skip the reverse pair by removing the result from the list#
    if not num % 2 == 0:
        return None
    CACHE = build_prime_cache(num)
    goldbach_list = []
    for prime in CACHE:
        result = num - prime
        if result in CACHE:
            goldbach_list.append((prime, result))
            CACHE.remove(result)

    return goldbach_list


tests = [
    (4, [(2,2)]),
    (6, [(3,3)]),
    (8, [(3,5)]),
    (10, [(3,7), (5,5)]),
    (100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]),
    (5, None) 
    ]

for test, expected in tests:

    print(expected == goldbach(test))