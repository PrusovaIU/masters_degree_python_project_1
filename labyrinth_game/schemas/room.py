from enum import Enum
from dataclasses import dataclass

from labyrinth_game.schemas.item import Items


class Rooms(Enum):
    """
    Список названий комнат
    """
    entrance = "entrance"
    hall = "hall"
    trap_room = "trap_room"
    library = "library"
    armory = "armory"
    treasure_room = "treasure_room"
    mirror_room = "mirror_room"
    illusion_corridor = "illusion_corridor"
    basement = "basement"
    torture_chamber = "torture_chamber"


class Directions(Enum):
    """
    Список названий направлений
    """
    north = "north"
    south = "south"
    east = "east"
    west = "west"
    up = "up"
    down = "down"


@dataclass
class RoomSchema:
    """
    Описание комнаты
    """
    description: str
    exits: dict[Directions, Rooms]
    items: list[Items]
    puzzle: tuple[str, str] | None
