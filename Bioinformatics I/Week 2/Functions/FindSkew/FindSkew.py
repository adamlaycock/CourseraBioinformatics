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

sequence = 'GAGCCACCGCGATA'

print(*find_patterns(sequence))