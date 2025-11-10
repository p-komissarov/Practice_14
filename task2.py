def read_integers() -> list:
    """
    Read integers from a single line, separated by spaces.
    Returns:
        list: A list of integers.
    """
    line = input().strip()
    if not line:
        return []
    return [int(token) for token in line.split()]


def remove_single_three(numbers: list) -> list:
    """
    Remove one value 3 from the list and return the new list.
    If the value 3 occurs more than once, a ValueError is raised.
    Args:
        numbers (list): A list of integers.
    Returns:
        list: A new list with one value 3 removed.
    Raises:
        ValueError: If the list does not contain exactly one value 3.
    """
    if numbers.count(3) != 1:
        raise ValueError("Исходный список должен содержать ровно одно значение 3.")
    idx = numbers.index(3)
    return numbers[:idx] + numbers[idx + 1:]


def main() -> None:
    try:
        numbers = read_integers()
        result = remove_single_three(numbers)
        print(result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()