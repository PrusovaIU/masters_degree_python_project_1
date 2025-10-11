from typing import NamedTuple

from .item import Items


class Puzzle(NamedTuple):
    text: str
    answer: str
    prize: Items | None


def solve_puzzle(puzzle: Puzzle) -> tuple[bool, Items | None]:
    """
    Функция для решения загадки

    :param puzzle: загадка.
    :return: Результат решения (true - загадка решена, иначе false) и приз.
    """
    print(f"Перед Вами загадка:\n"
          f"{puzzle.text}\n")
    answer: str = input("Ваш ответ: ").strip().lower()
    if answer == puzzle.answer:
        info = "Правильно!"
        prize = puzzle.prize
        if prize:
            info += f"Вы получаете {prize.value}."
        else:
            info += "Вы ничего не получаете."
        print(info)
        result = True
    else:
        print("Неправильно!")
        prize = None
        result = False
    return result, prize
