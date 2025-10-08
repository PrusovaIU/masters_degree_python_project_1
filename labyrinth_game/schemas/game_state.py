from pydantic import BaseModel, Field
from .room import Rooms, RoomSchema


class Player(BaseModel):
    """
    Описание состояния игрока
    """
    inventory: list[str] = Field(default_factory=list)


class GameState(BaseModel):
    """
    Состояние игры
    """
    player: Player = Field(default_factory=Player)
    current_room: RoomSchema = Field(default=Rooms.entrance)
    game_over: bool = Field(default=False)
    steps_taken: int = Field(default=0)
