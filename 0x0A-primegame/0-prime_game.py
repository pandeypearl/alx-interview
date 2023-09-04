#!/usr/bin/python3
"""
Defines The Prime Game
"""


def primeNumber(x):
    """
    Checking if number is prime.
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determining the winner of the prime game
    """
    if x < 1 or not nums or nums == []:
        return None
    rng = min(x, len(nums))
    maria = 0
    ben = 0
    player = 0
    for rng_it in range(rng):

        if nums[rng_it] < 2:
            ben += 1
        elif nums[rng_it] == 2:
            maria += 1
        else:
            player = True
            isPrime = 1
            j = list(range(2, nums[rng_it] + 1))

            while (isPrime):
                isPrime = 0
                for i in j:
                    if (primeNumber(i)):
                        isPrime = 1
                        player = not player
                        j = list(filter(lambda x: x % i != 0, j))

            if (player):
                ben += 1
            else:
                maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    return None
