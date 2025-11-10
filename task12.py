HOLES_LETTERS = set("abdegopq")


def count_holes_in_text(text: str) -> tuple:
    """
    Count the number of letters with holes and without holes in the text.
    Args:
        text (str): The input text.
    Returns:
        tuple: A tuple containing the count of letters with holes and without holes.
    """
    holes_count = 0
    non_holes_count = 0

    for char in text:
        if char.isalpha():
            if char in HOLES_LETTERS:
                holes_count += 1
            else:
                non_holes_count += 1

    return holes_count, non_holes_count


def words_with_multiple_holes(text: str) -> list:
    """
    Return a list of words that contain two or more letters with holes.
    Args:
        text (str): The input text.
    Returns:
        list: A list of words with two or more letters with holes.
    """
    words = text.split()
    result = []

    for word in words:
        count = sum(1 for char in word if char in HOLES_LETTERS)
        if count >= 2:
            result.append(word)

    return result


def main() -> None:
    text = input("Введите строку: ").lower()
    holes_count, non_holes_count = count_holes_in_text(text)
    words_with_holes = words_with_multiple_holes(text)

    print(holes_count, non_holes_count)
    print(words_with_holes)


if __name__ == "__main__":
    main()