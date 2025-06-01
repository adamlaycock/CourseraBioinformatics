def FindClumps(text: str, k: int, L: int, t:int):
    patterns = set()
    for i in range(len(text) - L + 1):
        window = text[i:i + L]
        pattern_counts = {}
        for j in range(L -  k + 1):
            pattern = window[j:j + k]
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        patterns.update([p for p, c in pattern_counts.items() if c >= t])
    return list(patterns)