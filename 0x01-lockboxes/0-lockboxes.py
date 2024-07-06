def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    total_keys = set(boxes[0]) | {0}  # Initialize with keys in the first box and box 0 itself
    added = True

    while added:
        added = False
        for box in range(len(boxes)):
            for key in boxes[box]:
                if key not in total_keys:
                    total_keys.add(key)
                    added = True

    return len(total_keys) == len(boxes)

# Example test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
