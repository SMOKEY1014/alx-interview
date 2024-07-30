#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.

The `canUnlockAll` function uses a breadth-first search (BFS) approach to
determine if all boxes can be opened given that each box may contain keys
to other boxes.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each element is a list of
        keys (box indices) available in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    opened = set()  # Set to track opened boxes
    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()

        if current_box not in opened:
            opened.add(current_box)
            # Add all boxes that can be opened with keys from the current box
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    queue.append(key)

    # Check if all boxes are opened
    return len(opened) == n
