import string


def words_from_sentence(sentence: str) -> list:
    """
    Return a list of unique words in a sentence without adjacent punctuation marks.
    Args:
        sentence (str): The input sentence.
    Returns:
        list: A list of unique words in lowercase.
    """
    if not sentence:
        return []

    tokens = sentence.split()
    unique_words = []
    seen = set()

    for token in tokens:
        word = token.strip(string.punctuation).lower()
        if word and word not in seen:
            unique_words.append(word)
            seen.add(word)

    return unique_words


def main() -> None:
    sentence = input().strip()
    words = words_from_sentence(sentence)
    print(words)


if __name__ == "__main__":
    main()