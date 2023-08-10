#!/usr/bin/python3
'''Minimum operations question.
'''


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Break down the given number n into its prime factors
    # The sum of those prime factors gives minimum operations
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
