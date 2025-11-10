import string


def words_from_sentence(sentence: str) -> list:
    """
    Return a list of words in a sentence without adjacent punctuation marks.
    Args:
        sentence (str): The input sentence.
    Returns:
        list: A list of words.
    """
    if not sentence:
        return []

    tokens = sentence.split()
    cleaned = [token.strip(string.punctuation) for token in tokens]
    return [word for word in cleaned if word]


def main() -> None:
    sentence = input().strip()
    words = words_from_sentence(sentence)
    print(words)


if __name__ == "__main__":
    main()