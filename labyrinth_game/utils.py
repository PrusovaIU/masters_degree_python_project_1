from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.player_actions import Commands
from labyrinth_game.schemas.puzzle import Puzzle
from labyrinth_game.schemas.room import Rooms, RoomSchema
from labyrinth_game.constants import ROOMS
from labyrinth_game.schemas.item import Inventory


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


def puzzle(
        current_room: RoomSchema,
        inventory: Inventory
) -> None:
    """
    Функция для решения загадки.

    :param current_room: текущая комната, в которой находится загадка.
    :param inventory: инвентарь игрока.
    :return: None
    """
    print(f"Перед Вами загадка:\n"
          f"{current_room.puzzle.text}\n")
    answer: str = input("Ваш ответ: ").strip().lower()
    if answer == current_room.puzzle.answer:
        current_room.puzzle = None
        info = "Правильно!"
        prize = current_room.puzzle.prize
        if prize:
            info += f"Вы получаете {prize.value}."
            inventory.append(prize)
        else:
            info += "Вы ничего не получаете."
        print(info)
    else:
        print("Неправильно!")
