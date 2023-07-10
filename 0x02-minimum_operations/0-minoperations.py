#!/usr/bin/env python3
""" Defines function minOPerations using
factorization """


def factorize(n):
    """
    Returns sum of prime factors of n
    or n if prime number
    """
    j = 2
    k = 0
    while j <= n:
        if n % j == 0:
            n = n // j
            k += j
            j -= 1
        j += 1
    return k


def minOperations(n):
    """
    Returns min number of operations or 0.
    """
    if not isinstance(n, int) or n < 2:
        return 0
    return factorize(n)
