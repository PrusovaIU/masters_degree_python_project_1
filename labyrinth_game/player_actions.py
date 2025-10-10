from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.schemas.room import Directions, RoomSchema, Rooms
from labyrinth_game.schemas.item import Items, add_item_to_inventory
from labyrinth_game.item_use_handlers import UseItemHandlerType, \
    USE_ITEMS_HANDLERS
from labyrinth_game.schemas.puzzle import solve_puzzle
from itertools import groupby
from labyrinth_game.exceptions import ExitException


def show_inventory(game_state: GameState) -> None:
    """
    Функция для вывода в консоль информации об объектах в инвентаре игрока.

    :param game_state: текущее состояние игры
    :return: None
    """
    if game_state.player.inventory:
        groups: dict[Items, list[Items]] = {
            key: list(group)
            for key, group in groupby(game_state.player.inventory)
        }
        info_strs = []
        for key, group in groups.items():
            istr = f"{len(group)} x {key.value}"
            info_strs.append(istr)
        info = "\n\t".join(info_strs)
        print(f"В вашем инвентаре: {info}")
    else:
        print("Инвентарь пуст")


def move(
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


def take(game_state: GameState, item_name: Items) -> None:
    """
    Функция для поднятия предмета из комнаты в инвентарь.

    :param game_state: текущее состояние игры.
    :param item_name: имя предмета.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    try:
        idx = current_room.items.index(item_name)
        if add_item_to_inventory(item_name, game_state.player.inventory):
            current_room.items.pop(idx)
    except ValueError:
        print("Такого предмета здесь нет.")


def use(game_state: GameState, item: Items) -> None:
    """
    Функция для использования предмета.

    :param game_state: текущее состояние игры.
    :param item: используемый предмет.
    :return: None.
    """
    handler: UseItemHandlerType = USE_ITEMS_HANDLERS[item]
    handler(game_state)


def exit(game_state: GameState) -> None:
    """
    Обработчик команды выхода из игры.

    :param game_state: состояние игры.
    :return: None.
    """
    while True:
        to_exit = input("Вы хотите выйти из игры? (y/n): ")
        if to_exit == "y":
            raise ExitException()
        elif to_exit == "n":
            return None
        else:
            print("Некорректный ввод!")


def solve(game_state: GameState) -> None:
    """
    Функция для обнаружения и решения загадки.

    :param game_state: состояние игры.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    if current_room.puzzle:
        success, prize = solve_puzzle(current_room.puzzle)
        if success:
            game_state.player.inventory.append(prize)
            current_room.puzzle = None
            if game_state.current_room == Rooms.treasure_room:
                print("Вы нашли сокровище!")
                game_state.game_over = True
    else:
        print("Загадок здесь нет.")
