#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """Returns a list of lists of numbers representing the Pascal triangle"""
    if n <= 0:
        return []

    # Initialize the Pascal triangle with zeros
    triangle = [0] * n

    for i in range(n):
        # Create a new row and fill the first and last indices with 1
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        # Calculate the values for the current row based on the previous row
        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = triangle[i - 1][j]  # Value from the previous row at index j
                b = triangle[i - 1][j - 1]  # Value from the previous row at index j-1
                new_row[j] = a + b

        triangle[i] = new_row

    return triangle
