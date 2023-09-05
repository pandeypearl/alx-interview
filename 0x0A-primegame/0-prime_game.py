#!/usr/bin/python3
"""
Defines The Prime Game
"""


def isPrime(x):
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
    Maria = 0
    Ben = 0
    player = 0
    for rng_it in range(rng):
        if nums[rng_it] < 2:
            Ben += 1
        elif nums[rng_it] == 2:
            Maria += 1
        else:
            player = True
            prime_number = 1
            n = list(range(2, nums[rng_it] + 1))
            while (prime_number):
                prime_number = 0
                for i in n:
                    if (isPrime(i)):
                        prime_number = 1
                        player = not player
                        n = list(filter(lambda x: x % i != 0, n))
            if (player):
                Ben += 1
            else:
                Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
