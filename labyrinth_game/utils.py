from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.constants import Commamds

def describe_current_room(game_state: GameState) -> None:
    """
    Функция для вывода в консоль описания текущей комнаты.

    :param game_state: состояние игры.
    :return: None.
    """
    current_room = game_state.current_room
    info = (f"Вы находитесь в {current_room.name}\n"
            f"{current_room.description}\n")
    if current_room.items:
        items = ", ".join(current_room.items)
        info += f"Заметные предметы:{items}\n"
    if current_room.exits:
        exists = ", ".join([exist.name for exist in current_room.exits.keys()])
        info += f"Выходы:{exists}\n"
    if current_room.puzzle:
        info += (f"Кажется, здесь есть загадка "
                 f"(используйте команду {Commamds.solve.name}).")
    print(f"Вы находитесь в {current_room.name}")