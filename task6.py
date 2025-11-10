import math


def find_divisors(num):
    """
    Function to find all divisors of a given integer.
    Args:
        num (int): The integer to find divisors for.
    Returns:
        list: A list of divisors of the integer.
    """
    divisors = set()  
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)  
    return list(divisors)


def main() -> None:
    try:
        num = int(input("Введите целое число: "))
        result = find_divisors(num)
        print("Список делителей числа:", result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()