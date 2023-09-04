# 0x08. Making Change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

+ Prototype: def makeChange(coins, total)
+ Return: fewest number of coins needed to meet total
    + If total is 0 or less, return 0
    + If total cannot be met by any number of coins you have, return -1
+ coins is a list of the values of the coins in your possession
+ The value of a coin will always be an integer greater than 0
+ You can assume you have an infinite number of each denomination of coin in the list
+ Your solution’s runtime will be evaluated in this task

| File | Description |
|------|:------------|
| [0-making_change.py](0-making_change.py) | Answer file |
| [0-main.py](0-main.py) | Test file |

Run Test file with <code>./0-main.py</code> or <code>python 0-main.py</code> in the terminal.