import string


def read_text() -> str:
    """
    Read multiple lines of text until an empty line is entered.
    Returns:
        str: The concatenated text from all lines.
    """
    print("Введите текст (пустая строка — конец ввода):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return " ".join(lines)


def get_words(text: str) -> list:
    """
    Extract words from text, removing adjacent punctuation and converting to lowercase. 
    Args:
        text (str): The input text.
    Returns:
        list: A list of cleaned words.
    """
    words = []
    for token in text.split():
        word = token.strip(string.punctuation).lower()
        if word:
            words.append(word)
    return words


def sort_words_by_frequency(words: list) -> list:
    """
    Sort words by their frequency in descending order. If frequencies are equal,
    maintain the order of first appearance.
    Args:
        words (list): A list of words.
    Returns:
        list: A list of words sorted by frequency.
    """
    frequency = {}
    order = {}

    for index, word in enumerate(words):
        frequency[word] = frequency.get(word, 0) + 1
        if word not in order:
            order[word] = index

    sorted_words = sorted(frequency.keys(),
                          key=lambda w: (-frequency[w], order[w]))
    return sorted_words


def main() -> None:
    text = read_text()
    words = get_words(text)
    sorted_words = sort_words_by_frequency(words)

    for word in sorted_words:
        print(word)


if __name__ == "__main__":
    main()