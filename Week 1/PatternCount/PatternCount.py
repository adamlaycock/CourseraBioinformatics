def count_pattern(text: str, pattern: str) -> float:
    """_summary_

    Args:
        text (str): Text to search for pattern within.
        pattern (str): Pattern to find.

    Returns:
        float: Number of times the pattern occurs in the text.
    """
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

with open('dataset_30272_6.txt', 'r') as file:
    text = file.read()
pattern = 'CAGCTAACA'

print(count_patterns(text, pattern))