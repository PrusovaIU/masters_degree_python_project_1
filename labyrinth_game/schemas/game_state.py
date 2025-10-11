from dataclasses import dataclass

from labyrinth_game.constants.rooms_list import ROOMS
from labyrinth_game.inventory import Inventory

from .room import Rooms, RoomSchema


@dataclass
class Player:
    """
    Описание состояния игрока
    """
    inventory: Inventory


@dataclass
class GameState:
    """
    Состояние игры
    """
    player: Player
    current_room: Rooms
    game_over: bool
    steps_taken: int


def initial_state() -> GameState:
    player = Player(inventory=[])
    return GameState(
        player=player,
        current_room=Rooms.entrance,
        game_over=False,
        steps_taken=0
    )


def get_room(game_state: GameState) -> RoomSchema:
    """
    Получить текущую комнату из состояния игры.

    :param game_state: текущее состояние игры.
    :return: описание текущей комнаты.
    """
    current_room_name: Rooms = game_state.current_room
    return ROOMS[current_room_name]
