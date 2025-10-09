from enum import Enum
from collections.abc import Callable
from labyrinth_game.schemas.game_state import GameState


class Commands(Enum):
    solve = "solve"
    exit = "exit"


def _exit(game_state: GameState) -> None:
    """
    Обработчик команды выхода из игры.

    :param game_state: состояние игры.
    :return: None.
    """
    while True:
        to_exit = input("Вы хотите выйти из игры? (да/нет): ")
        if to_exit == "да":
            game_state.game_over = True
            return None
        elif to_exit == "нет":
            return None
        else:
            print("Некорректный ввод!")


commands_handler: dict[Commands, Callable[[GameState], None]] = {
    Commands.exit: _exit
}
