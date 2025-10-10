from labyrinth_game.constants import ROOMS
from labyrinth_game.commands import Commands
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.schemas.room import Rooms, RoomSchema


def describe_current_room(game_state: GameState) -> None:
    """
    Функция для вывода в консоль описания текущей комнаты.

    :param game_state: состояние игры.
    :return: None.
    """
    current_room_name: Rooms = game_state.current_room
    current_room: RoomSchema = ROOMS[current_room_name]
    info = (f"Вы находитесь в {current_room_name.value}\n"
            f"{current_room.description}\n")
    if current_room.items:
        items = ", ".join([item.value for item in current_room.items])
        info += f"Заметные предметы:{items}\n"
    if current_room.exits:
        exists = ", ".join([exist.name for exist in current_room.exits.keys()])
        info += f"Выходы:{exists}\n"
    if current_room.puzzle:
        info += (f"Кажется, здесь есть загадка "
                 f"(используйте команду {Commands.solve.name}).")
    print(info)
