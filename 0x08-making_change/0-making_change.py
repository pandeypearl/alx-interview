"""
makChange function
"""

def makeChange(coins, total):
    """
    Determines fewest number of coins
    needed to meet given amount total
    """
    if total <= 0:
        return 0
    if not coins or min(coins) > total:
        return -1

    n_coins = 0
    coins.sort(reverse=True)

    i = 0
    while i < len(coins):
        if coins[i] <= total:
            n_coins += total // coins[i]
            total = total % coins[i]
        i += 1
        
    if total == 0:
        return n_coins
    else:
        return -1