from collections import Counter

from labyrinth_game.constants.direction import Directions
from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.exceptions import ExitException
from labyrinth_game.inventory import add_item_to_inventory
from labyrinth_game.item_use_handlers import (USE_ITEMS_HANDLERS,
                                              UseItemHandlerType)
from labyrinth_game.rooms_functional import describe_current_room
from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.schemas.puzzle import solve_puzzle
from labyrinth_game.schemas.room import RoomSchema
from labyrinth_game.environment_actions import random_event
from labyrinth_game.exceptions import DeadException


def show_inventory(game_state: GameState) -> None:
    """
    Функция для вывода в консоль информации об объектах в инвентаре игрока.

    :param game_state: текущее состояние игры
    :return: None
    """
    if game_state.player.inventory:
        info_strs = []
        for key, count in Counter(game_state.player.inventory).items():
            istr = f"{count} x {key.value}"
            info_strs.append(istr)
        info = "\n\t".join(info_strs)
        print(f"В вашем инвентаре:\n\t{info}")
    else:
        print("Инвентарь пуст")


def move(
        game_state: GameState,
        direction_name: str
) -> None:
    """
    Функция для перемещения игрока в другую комнату.

    :param game_state: текущее состояние игры.
    :param direction_name: направление движения игрока.
    :return: None.

    :raises DeadException: если игрок умер.
    """
    current_room: RoomSchema = get_room(game_state)
    direction = Directions(direction_name)
    try:
        game_state.current_room = current_room.exits[direction]
        game_state.steps_taken += 1
        random_event(game_state)
        if game_state.player.hp <= 0:
            raise DeadException("Вы умерли!")
        describe_current_room(game_state)
    except KeyError:
        print("Вы не можете пойти в эту сторону")


def take(game_state: GameState, item_name: str) -> None:
    """
    Функция для поднятия предмета из комнаты в инвентарь.

    :param game_state: текущее состояние игры.
    :param item_name: имя предмета.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    item = Items(item_name)
    try:
        idx = current_room.items.index(item)
        if add_item_to_inventory(item, game_state.player.inventory):
            current_room.items.pop(idx)
    except ValueError:
        print("Такого предмета здесь нет.")


def use(game_state: GameState, item_name: str) -> None:
    """
    Функция для использования предмета.

    :param game_state: текущее состояние игры.
    :param item_name: имя используемого предмета.
    :return: None.
    """
    item = Items(item_name)
    handler: UseItemHandlerType = USE_ITEMS_HANDLERS[item]
    handler(game_state)


def game_exit(game_state: GameState) -> None:
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


def look_around(game_state: GameState) -> None:
    """
    Функция для вывода информации о текущей комнате.

    :param game_state: текущее состояние игры.
    :return: None.
    """
    describe_current_room(game_state)
