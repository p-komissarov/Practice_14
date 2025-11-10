def sort_string_characters(text: str) -> str:
    """
    Sort the characters of the input string in ascending order.
    Args:
        text (str): The input string.
    Returns: 
        str: The string with characters sorted in ascending order.
    """
    chars = list(text)      
    chars.sort()          
    sorted_text = ''.join(chars)  
    return sorted_text


def main() -> None:
    text = input("Введите строку: ")
    result = sort_string_characters(text)
    print("Отсортированная строка:", result)


if __name__ == "__main__":
    main()