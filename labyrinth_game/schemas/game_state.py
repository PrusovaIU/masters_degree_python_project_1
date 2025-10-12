from dataclasses import dataclass

from labyrinth_game.constants.room import Rooms
from labyrinth_game.constants.rooms_list import ROOMS
from labyrinth_game.inventory import Inventory
from labyrinth_game.constants.direction import Directions
from labyrinth_game.exceptions import GetNextRoomException

from .room import RoomSchema


@dataclass
class Player:
    """
    Описание состояния игрока
    """
    inventory: Inventory
    hp: int


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
    """
    Инициализировать состояние игры.

    :return: начальное состояние игры.
    """
    player = Player(
        inventory=[],
        hp=30
    )
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


def get_next_room(
        current_room: RoomSchema,
        direction_name: str
) -> tuple[Rooms, RoomSchema]:
    """"""
    try:
        direction = Directions(direction_name)
        next_room_name = current_room.exits[direction]
        return next_room_name, ROOMS[next_room_name]
    except ValueError:
        print("Неизвестное направление")
        raise GetNextRoomException(direction_name)
    except KeyError:
        print("Вы не можете пойти в эту сторону")
        raise GetNextRoomException(direction_name)
