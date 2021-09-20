def build_prime_cache(num):
    # to create a cache will all the primes in the range from 2 to the input number#
    # I SAW YOUR SOLUTION AND IT IS MUCH BETTER AND WILL USE MUCH LESS RESOURCES #
    # However I wanted to keep it genuine #
    prime_nums = []
    for number in range(2, num + 1):
        prime = True
        for factor in range(2, number):
            if number % factor == 0:
                prime = False   
        if prime:
            prime_nums.append(number)
    return prime_nums


def prime_factorization(num):
    # we set a base case where the input num is reduced to 1 #
    # we start iterating through our primes in the CACHE #
    # checking the number of occurencies with an inner while loop #
    CACHE = build_prime_cache(num)
    prime_factors = []
    power_counter = 0
    while not num == 1:
        for prime in CACHE:
            while num % prime == 0:
                power_counter += 1
                num = num // prime

            if power_counter > 0:
                prime_factors.append((prime, power_counter))
            power_counter = 0

    return prime_factors




tests = [
    (10, [(2, 1), (5, 1)]),
    (14, [(2, 1), (7, 1)]),
    (356, [(2, 2), (89, 1)]),
    (89, [(89, 1)]),
    (1000, [(2, 3), (5, 3)]) 
    ]

for test, expected in tests:

    print(expected == prime_factorization(test))