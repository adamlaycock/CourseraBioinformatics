def find_patterns(text: str, pattern: str) -> list:
    """_summary_

    Args:
        text (str): Text in which patterns are searched for.
        pattern (str): Pattern to find.

    Returns:
        list: List of indices where a pattern begins in the text.
    """
    starts = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            starts.append(i)

    return starts

with open('dataset_30273_5.txt', 'r') as file:
    text = file.read()
pattern = 'AGAATCGAG'

print(*find_patterns(text, pattern))