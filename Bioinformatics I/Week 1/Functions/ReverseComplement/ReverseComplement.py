def reverse_complement(text: str) -> str:
    """_summary_

    Args:
        text (str): Text to be converted to its revcomp.

    Returns:
        str: Text after conversion.
    """
    return text.translate(str.maketrans('ATGC', 'TACG'))[::-1]

with open('dataset_30273_2.txt', 'r') as file:
    text = file.read()

print(reverse_complement(text))
