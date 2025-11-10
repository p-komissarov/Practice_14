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


def cyclic_shift(lst: list, command: str) -> list:
    """
    Perform a cyclic shift on the list based on the command.
    Args:
        lst (list): The list of integers to be shifted.
        command (str): The shift command (e.g., 'R5' for right shift by 5, 'L3' for left shift by 3).
    Returns:
        list: The list after performing the cyclic shift.
    """
    if not lst or not command:
        return lst

    direction = command[0].upper()
    try:
        positions = int(command[1:])
    except ValueError:
        print("Неверная команда.")
        return lst

    n = len(lst)
    positions %= n 

    if direction == 'R':
        return lst[-positions:] + lst[:-positions]
    elif direction == 'L':
        return lst[positions:] + lst[:positions]
    else:
        print("Неверное направление. Используйте R или L.")
        return lst


def main() -> None:
    lst = read_list("Введите список целых чисел: ")
    command = input("Введите команду сдвига (например, R5 или L3): ").strip()
    lst = cyclic_shift(lst, command)
    print("Список после сдвига:", lst)


if __name__ == "__main__":
    main()