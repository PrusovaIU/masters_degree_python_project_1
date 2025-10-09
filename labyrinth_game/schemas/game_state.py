from .room import Rooms
from dataclasses import dataclass


@dataclass
class Player:
    """
    Описание состояния игрока
    """
    inventory: list[str]


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
