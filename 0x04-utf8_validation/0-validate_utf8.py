#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def byte_sequence_count(byte):
        """Returns the number of bytes in a UTF-8 sequence"""
        binary_representation = bin(byte)[2:].rjust(8, "0")
        if binary_representation.startswith("0"):
            return 1
        elif binary_representation.startswith("110"):
            return 2
        elif binary_representation.startswith("1110"):
            return 3
        elif binary_representation.startswith("11110"):
            return 4
        else:
            return -1

    i = 0

    while i < len(data):
        sequence_count = byte_sequence_count(data[i])
        if sequence_count == -1:
            return False

        i += 1
        if sequence_count == 1:
            continue

        if i + sequence_count - 1 > len(data):
            return False

        for j in range(sequence_count - 1):
            if not (data[i + j] >> 6 == 0b10):
                return False

        i += sequence_count - 1

    return True
