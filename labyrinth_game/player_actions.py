from enum import Enum
from typing import Callable, Any

from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.schemas.room import Directions, RoomSchema, Rooms
from labyrinth_game.schemas.item import USE_ITEMS_HANDLERS, Items


class Commands(Enum):
    solve = "solve"
    go = "go"
    exit = "exit"


def _show_inventory(game_state: GameState) -> None:
    """
    Функция для вывода в консоль информации об объектах в инвентаре игрока.

    :param game_state: текущее состояние игры
    :return: None
    """
    if game_state.player.inventory:
        objects = "\n\t".join(game_state.player.inventory)
        print(f"В вашем инвентаре:{objects}")
    else:
        print("Инвентарь пуст")


def _move_player(
        game_state: GameState,
        direction: Directions
) -> None:
    """
    Функция для перемещения игрока в другую комнату.

    :param game_state: текущее состояние игры.
    :param direction: направление движения игрока.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    try:
        game_state.current_room = current_room.exits[direction]
        game_state.steps_taken += 1
    except KeyError:
        print("Вы не можете пойти в эту сторону")


def _take_item(game_state: GameState, item_name: Items) -> None:
    """
    Функция для поднятия предмета из комнаты в инвентарь.

    :param game_state: текущее состояние игры.
    :param item_name: имя предмета.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    try:
        current_room.items.remove(item_name)
        game_state.player.inventory.append(item_name)
        print("Вы подняли: " + item_name.value)
    except ValueError:
        print("Такого предмета здесь нет.")


def _use_item(game_state: GameState, item: Items) -> None:
    handler = USE_ITEMS_HANDLERS[item]



def _exit(game_state: GameState) -> None:
    """
    Обработчик команды выхода из игры.

    :param game_state: состояние игры.
    :return: None.
    """
    while True:
        to_exit = input("Вы хотите выйти из игры? (y/n): ")
        if to_exit == "y":
            game_state.game_over = True
            return None
        elif to_exit == "n":
            return None
        else:
            print("Некорректный ввод!")


COMMAND_HANDLERS: dict[Commands, Callable[[GameState, Any], None]] = {
    Commands.go: _move_player
}

def process_command(game_state: GameState, command: str) -> None:
    command, args = command.split(" ", maxsplit=1)
    command = Commands(command)
    if command == Commands.exit:
        _exit(game_state)
    else:
        command_handler: Callable[[GameState, Any], None] = \
            COMMAND_HANDLERS[command]
        command_handler(command, args)




def get_input(game_state: GameState, promt: str="> ") -> None:
    """
    Функция для получения ввода пользователя.

    :param game_state: текущее состояние игры.
    :param promt: строка с просьбой ввести команду.
    :return: None.
    """
    try:
        command = Commands(input(promt))
        command_handler: Callable[[GameState], None] = \
            COMMAND_HANDLERS[command]
        command_handler(game_state)
    except ValueError:
        print("Некорректная команда")
    except KeyError:
        print("Команда не реализована. Обратитесь к разработчику.")
    except (KeyboardInterrupt, EOFError):
        game_state.game_over = True
