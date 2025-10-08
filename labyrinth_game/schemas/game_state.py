from pydantic import BaseModel, Field
from .room import Rooms

class GameState(BaseModel):
    """
    Состояние игры
    """
    player_inventory: list[str] = Field(default_factory=list)
    current_room: str = Field(default=Rooms.entrance)
    game_over: bool = Field(default=False)
    steps_taken: int = Field(default=0)
