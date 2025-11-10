def read_ten_integers() -> list:
    """
    Read 10 integers from standard input.
    Returns:
        list: A list of 10 integers.
    """
    numbers = []
    print("Введите 10 целых чисел (через пробел или по одному на строке):")
    while len(numbers) < 10:
        try:
            line = input().strip()
            if not line:
                continue
            for token in line.split():
                if len(numbers) >= 10:
                    break
                numbers.append(int(token))
        except ValueError:
            print("Ошибка: вводите только целые числа. Повторите ввод строки.")
    return numbers


def neighbor_sums(numbers: list) -> list:
    """
    Return sums of neighbors for interior elements.
    Args:
        numbers (list): A list of integers.
    Returns:
        list: A list of sums of neighbors for each interior element.
    """
    n = len(numbers)
    if n < 3:
        return []
    return [numbers[i - 1] + numbers[i + 1] for i in range(1, n - 1)]


def main() -> None:
    numbers = read_ten_integers()
    result = neighbor_sums(numbers)
    print(result)


if __name__ == "__main__":
    main()