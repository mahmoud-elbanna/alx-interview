#!/usr/bin/python3

'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    # Create a set to keep track of the boxes that have been visited
    visited = set()
    visited.add(0)  # Mark the first box as visited

    # Create a stack to store the keys
    stack = [0]  # Start with the keys from the first box

    # Iterate through the stack until it's empty
    while stack:
        box = stack.pop()  # Get the top box from the stack

        # Iterate through the keys in the current box
        for key in boxes[box]:
            # If the key opens a new box and it hasn't been visited yet, add it to the stack and mark it as visited
            if key < len(boxes) and key not in visited:
                stack.append(key)
                visited.add(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
    

