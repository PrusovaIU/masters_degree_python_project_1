from labyrinth_game.constants.item import Items
from labyrinth_game.schemas.puzzle import Puzzle
from labyrinth_game.schemas.room import RoomSchema
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.constants.room import Rooms


def _get_answer(puzzle: Puzzle) -> tuple[bool, Items | None]:
    """
    Функция для получения ответа на загадку.

    :param puzzle: загадка.

    :return: Результат решения (true - загадка решена, иначе false) и приз,
        если есть.
    """
    print(f"Перед Вами загадка:\n"
          f"{puzzle.text}\n")
    answer: str = input("Ваш ответ: ").strip().lower()
    if answer in puzzle.answer:
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


def _get_prize(
        game_state: GameState,
        prize: Items | None
) -> None:
    """
    Функция для получения приза.

    :param game_state: состояние игры.
    :param prize: приз.
    :return: None.
    """
    if prize:
        game_state.player.inventory.append(prize)
    if game_state.current_room == Rooms.treasure_room:
        print("Вы нашли сокровище!")
        game_state.game_over = True


def solve_puzzle(
        game_state: GameState,
        current_room: RoomSchema
) -> None:
    """
    Функция для решения загадки

    :param game_state: состояние игры.
    :param current_room: комната, в которой находится загадка.
    :return: Результат решения (true - загадка решена, иначе false) и приз.
    """
    success, prize = _get_answer(current_room.puzzle)
    if success:
        current_room.puzzle = None
        _get_prize(game_state, prize)

