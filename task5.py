def read_numbers() -> list:
    """
    Count integers from a single line, separated by spaces.
    Returns:
        list: A list of integers.
    """
    line = input("Введите целые числа через пробел: ").strip()
    if not line:
        return []
    return [int(token) for token in line.split()]


def average(numbers: list) -> float:
    """
    Calculate the average of a list of integers.
    Args:
        numbers (list): A list of integers.
    Returns:
        float: The average of the integers in the list.
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main() -> None:
    try:
        numbers = read_numbers()
        result = average(numbers)
        print("Среднее значение элементов списка:", result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()