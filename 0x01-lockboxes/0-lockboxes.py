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
    if boxes is None:
        return False
    if not isinstance(boxes, list):
        return False
    if boxes == []:
        return False
    if boxes == [[]]:
        return True
    if boxes[0] == [] and len(boxes) > 1:
        return False
    for box_key in boxes:
        if not isinstance(box_key, list):
            return False
        else:
            for value in box_key:
                if not isinstance(value, int):
                    return False
    Unlocked = [False for box_key in boxes]
    Unlocked[0] = True
    Open = [False for box_key in boxes]
    while [True for box_key in range(len(boxes))
            if Open[box_key] is False and Unlocked[box_key] is True]:
        for i in range(len(boxes)):
            if Unlocked[i] is True:
                Open[i] = True
                for box_key in boxes[i]:
                    try:
                        Unlocked[box_key] = True
                    except Exception:
                        pass
    return False not in Unlocked
