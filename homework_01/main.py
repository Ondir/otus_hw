"""
Домашнее задание №1
Функции и структуры данных
"""

def is_prime(number):

    # Python program to check if
    # given number is prime or not

    # If given number is greater than 1
    if number > 1:

        # Iterate from 2 to n / 2
        for i in range(2, int(number / 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (number % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == 'even':
        return [i for i in numbers if i % 2 == 0]
    if filter_type == 'odd':
        return [i for i in numbers if i % 2 == 1]
    if filter_type == 'prime':
        return [i for i in filter(is_prime, numbers)]


list_numbers = filter_numbers([1, 2, 3], ODD)
print(list_numbers)

event_numbers = filter_numbers([2, 3, 4, 5], EVEN)
print(event_numbers)

power_num = power_numbers(1, 2, 5, 7)
print(power_num)

prime_num = filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], PRIME)
print(prime_num)