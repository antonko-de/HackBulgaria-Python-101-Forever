def  sum_matrix(m):
    sum_total = 0
    #initiate an intiger to store the sume of the digits in the matrix#
    for i in m:
        sum_total += sum(i)
    return sum_total


tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],55)
]

for test, expected in tests:
    print(expected == sum_matrix(test))