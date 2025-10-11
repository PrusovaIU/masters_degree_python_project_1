from dataclasses import dataclass

from labyrinth_game.constants.direction import Directions
from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.schemas.puzzle import Puzzle


@dataclass
class RoomSchema:
    """
    Описание комнаты
    """
    description: str
    exits: dict[Directions, Rooms]
    items: list[Items]
    puzzle: Puzzle | None
