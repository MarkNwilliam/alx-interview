#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    # List to keep track of unlocked boxes
    unlocked = [False] * len(boxes)
    # Mark the first box as unlocked
    unlocked[0] = True
    
    # Keys we have
    keys = [0]

    while keys:
        current_key = keys.pop()

        # Unlocking boxes using current key
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    # If any box remains locked, return False, otherwise True
    return all(unlocked)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
