def read_list(prompt: str) -> list:
    """
    Read a list of integers from a single line of input, separated by spaces.
    Args:
        prompt (str): The prompt to display to the user.
    Returns:
        list: A list of integers.
    """
    line = input(prompt).strip()
    if not line:
        return []
    return [int(x) for x in line.split()]


def main() -> None:
    try:
        lst1 = read_list("Введите первый список: ")
        lst2 = read_list("Введите второй список: ")

        start = int(input("Введите начальный индекс диапазона: "))
        end = int(input("Введите конечный индекс диапазона: "))

        start_idx = start - 1
        end_idx = end

        slice_to_move = lst1[start_idx:end_idx][::-1]
        lst2.extend(slice_to_move)

        del lst1[start_idx:end_idx]

        print("Первый список после изменений:", lst1)
        print("Второй список после изменений:", lst2)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()