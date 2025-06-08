def FindClumps(text: str, k: int, L: int, t:int):
    """_summary_

    Args:
        text (str): Text in which clumps are searched for.
        k (int): Length of the kmers to be found.
        L (int): Length of the window to look for kmers in.
        t (int): Number of times a kmer must appear in a window to be logged.

    Returns:
        patterns: kmers which appear t times in some window of length L.
    """
    patterns = set()
    for i in range(len(text) - L + 1):
        window = text[i:i + L]
        pattern_counts = {}
        for j in range(L -  k + 1):
            pattern = window[j:j + k]
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        patterns.update([p for p, c in pattern_counts.items() if c >= t])
    return list(patterns)

with open('dataset_30274_5.txt', 'r') as file:
    text = file.read()

k = 10
L = 100
t = 4

print(*FindClumps(text, k, L, t))