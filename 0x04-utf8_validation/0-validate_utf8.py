#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Check if the given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers representing UTF-8 encoded data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    # Number of expected continuation bytes for the current UTF-8 character
    remaining_bytes = 0

    # Iterate over each integer in the data
    for num in data:
        if remaining_bytes == 0:
            # If no continuation bytes are expected, check the byte's pattern

            if num >> 5 == 0b110:
                # 2-byte character (pattern: 110xxxxx)
                remaining_bytes = 1
            elif num >> 4 == 0b1110:
                # 3-byte character (pattern: 1110xxxx)
                remaining_bytes = 2
            elif num >> 3 == 0b11110:
                # 4-byte character (pattern: 11110xxx)
                remaining_bytes = 3
            elif num >> 7 == 0b1:
                # Invalid start of a continuation byte (pattern: 10xxxxxx)
                return False
        else:
            # Continuation byte expected, check if the byte matches the pattern (10xxxxxx)
            if num >> 6 != 0b10:
                return False

            # Decrement the count of remaining continuation bytes
            remaining_bytes -= 1

    # If all bytes have been processed and there are no remaining bytes, the encoding is valid
    return remaining_bytes == 0
