from math import floor, sin


def user_input(promt: str, allowed_answer: list[str]) -> str:
    """
    Функция для получения ввода пользователя.

    :param promt: текст для вывода в консоль.
    :param allowed_answer: список допустимых ответов.
    :return: введенный пользователем ответ.
    """
    info = f"{promt} ({'/'.join(allowed_answer)}): "
    while True:
        command = input(info).strip().lower()
        if command not in allowed_answer:
            print("Неверная команда!")
        else:
            return command


def pseudo_random(seed: int, modulo: int) -> int:
    """
    Генерирует псевдослучайное число на основе seed и modulo.

    :param seed: начальное значение (например, количество шагов).
    :param modulo: верхняя граница диапазона (результат будет [0, modulo)).
    :return: псевдослучайное целое число.
    """
    seed_sin = sin(seed * 12.9898)
    hash_value = seed_sin * 43758.5453
    fractional_part = hash_value - floor(hash_value)
    result = int(fractional_part * modulo)
    return result
