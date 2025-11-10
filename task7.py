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


def sum_even_odd(numbers: list) -> tuple:
    """
    Calculate the sums of even and odd integers in a list.
    Args:
        numbers (list): A list of integers.
    Returns:
        tuple: A tuple containing the sum of even integers and the sum of odd integers.
    """
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum


def main() -> None:
    try:
        numbers = read_numbers()
        even_sum, odd_sum = sum_even_odd(numbers)
        print("Сумма чётных чисел:", even_sum)
        print("Сумма нечётных чисел:", odd_sum)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()