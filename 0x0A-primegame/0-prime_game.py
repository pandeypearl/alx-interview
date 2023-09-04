#!/usr/bin/python3
"""
Defines The Prime Game
"""


def primeNumber(n):
    """
    Checking if number is prime.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isWinner(n, numbers):
    """
    Determining the winner of the prime game
    """
    if n < 1 or not numbers or numbers == []:
        return None
    rng = min(n, len(numbers))
    maria = 0
    ben = 0
    player = 0
    for rng_it in range(rng):

        if numbers[rng_it] < 2:
            ben += 1
        elif numbers[rng_it] == 2:
            maria += 1
        else:
            player = True
            isPrime = 1
            j = list(range(2, numbers[rng_it] + 1))

            while (isPrime):
                isPrime = 0
                for i in j:
                    if (primeNumber(i)):
                        isPrime = 1
                        player = not player
                        j = list(filter(lambda n: n % i != 0, j))

            if (player):
                ben += 1
            else:
                maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    return None
