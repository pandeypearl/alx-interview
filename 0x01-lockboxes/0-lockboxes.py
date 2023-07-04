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
        for value in boxes[key]:
            if value not in keys:
                keys.append(value)
    if len(keys) == len(boxes):
        return True
    return False
