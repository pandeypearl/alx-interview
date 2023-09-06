#!/usr/bin/python3
"""
Defines The Prime Game
"""


def isWinner(x, nums):
    """
    Determining the winner of the prime game
    """
    if x < 1 or not nums:
        return None
    Maria = 0
    Ben = 0
    n = max(nums)
    prime_exists = [True for _ in range(1, n + 1, 1)]
    prime_exists[0] = False
    for i, isPrime in enumerate(prime_exists, 1):
        if i == 1 or not isPrime:
            continue
        for j in range(i + i, n + 1, i):
            prime_exists[j - 1] = False
    for _, n in zip(range(x), nums):
        prime_count = len(list(filter(lambda x: x, prime_exists[0: n])))
        Ben += prime_count % 2 == 0
        Maria += prime_count % 2 == 1
    if Maria == Ben:
        return None
    return 'Maria' if Maria > Ben else 'Ben'
