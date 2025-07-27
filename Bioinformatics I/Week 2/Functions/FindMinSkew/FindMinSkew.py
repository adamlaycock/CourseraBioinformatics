import numpy as np

def find_skew(
    sequence: str
) -> list:
    """
    Calculates the skew value for each base in a sequence and returns the
    result as a list.

    Args:
        sequence (str): String containing the sequence to be evaluated.

    Returns:
        list: List containing the skew value at each base in the sequence.
    """
    skew = [0]

    for base in sequence.upper():
        if base == 'G':
            skew.append(skew[-1] + 1)
        elif base == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])

    return skew


def find_min_skew(
    skew: list
) -> list:
    """

    Args:
        skew (list): _description_

    Returns:
        list: _description_
    """
    min_idx = [idx for idx, val in enumerate(skew) if val == min(skew)]
    
    return min_idx

with open('dataset_30277_10.txt', 'r') as file:
    text = file.read()

print(*find_min_skew(find_skew(text)))