#!/usr/bin/python3
"""
Lockboxes Solution
"""


def canUnlockAll(boxes):
    """
    Function to determine if all boxes can be unlocked.
    Returns True if all boxes can be unlocked
    and False otherwise
    """
    box_keys = [0]
    pending = []
    for value in range(1, len(boxes)):
        if value in box_keys:
            for box_key in boxes[value]:
                box_keys.append(box_key)
        else:
            pending.append(value)
    for value in pending:
        if value in box_keys:
            for box_key in boxes[value]:
                box_keys.append(box_key)
        else:
            return False
    return True
