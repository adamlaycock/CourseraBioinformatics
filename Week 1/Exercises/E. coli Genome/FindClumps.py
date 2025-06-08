def FindClumps(text: str, k: int, L: int, t: int):
    """_summary_

    Args:
        text (str): Text in which clumps are searched for.
        k (int): Length of the kmers to be found.
        L (int): Length of the window to look for kmers in.
        t (int): Number of times a kmer must appear in a window to be logged.

    Returns:
        patterns: kmers which appear t times in some window of length L.
    """
    from collections import defaultdict

    n = len(text)
    clumps = set()
    kmer_counts = defaultdict(int)

    for i in range(L - k + 1):
        kmer = text[i:i+k]
        kmer_counts[kmer] += 1

    for kmer, count in kmer_counts.items():
        if count >= t:
            clumps.add(kmer)

    for i in range(1, n - L + 1):
        first_kmer = text[i-1:i-1+k]
        kmer_counts[first_kmer] -= 1

        new_kmer = text[i + L - k:i + L]
        kmer_counts[new_kmer] += 1
        
        if kmer_counts[new_kmer] >= t:
            clumps.add(new_kmer)

    return list(clumps)

with open('E_coli.txt', 'r') as file:
    text = file.read()

k = 9
L = 500
t = 3

print(len(FindClumps(text, k, L, t)))