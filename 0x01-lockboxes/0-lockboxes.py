#!/usr/bin/python3
"""
Lockboxes Solution
"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be unlocked.
    """
    box_keys = [0]

    for box_key in box_keys:
        for value in boxes[box_key]:
            if value not in box_keys:
                box_keys.append(value)

    if len(box_keys) == len(boxes):
        return True

    return False
