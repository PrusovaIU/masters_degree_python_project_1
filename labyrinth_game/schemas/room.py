from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Rooms(Enum):
    """
    Список названий комнат
    """
    entrance = "entrance"
    hall = "hall",
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


class RoomSchema(BaseModel):
    """
    Описание комнаты
    """
    description: str
    exits: dict[Directions, Rooms]
    items: list[str]
    puzzle: Optional[tuple[str, str]]
