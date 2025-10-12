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
    # текстовое описание комнаты:
    description: str
    # список выходов из комнаты:
    exits: dict[Directions, Rooms]
    # список предметов в комнате:
    items: list[Items]
    # загадка в комнате, если есть:
    puzzle: Puzzle | None
    # наличие ловушки в комнате:
    trap: bool
    # предмет, которым отрывается комната. Если None, то комната не заперта:
    lock: Items | None
