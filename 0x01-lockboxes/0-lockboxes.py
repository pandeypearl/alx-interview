#!/usr/bin/python3
"""
Lockboxes Solution
"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be unlocked.
    """
    keys = [0]
    for key in keys:
        for val in boxes[key]:
            if val not in keys:
                keys.append(val)
    if len(keys) == len(boxes):
        return True
    return False
