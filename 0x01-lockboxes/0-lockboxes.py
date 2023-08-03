#!/usr/bin/python3
"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""

def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """
    # Set to keep track of boxes we've unlocked or visited
    visited = set()

    # Queue for BFS approach (starts with box 0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        # If we've already processed this box, continue to the next one
        if current_box in visited:
            continue

        visited.add(current_box)
        
        for key in boxes[current_box]:
            # Only add the key to the queue if it's a valid box number
            # and hasn't been visited yet
            if key < len(boxes) and key not in visited:
                queue.append(key)

    # If we've visited all the boxes, return True
    return len(visited) == len(boxes)

# Sample Test Cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

