def count_patterns(text: str, k: int) -> list:
    """_summary_

    Args:
        text (str): Text to search for patterns within.
        k (int): Length of the k-mer patterns to find.

    Returns:
        list: List of most frequent k-mers.
    """
    pattern_counts = {}
    for i in range(len(text) -  k + 1):
        pattern = text[i:i + k]
        pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1

    max_count = max(pattern_counts.values())
    frequent_patterns = [p for p, c in pattern_counts.items() if c == max_count]

    return frequent_patterns