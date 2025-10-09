from enum import Enum
from collections.abc import Callable
from labyrinth_game.schemas.game_state import GameState


class Commands(Enum):
    solve = "solve"


commands_handler: dict[Commands, Callable[[GameState], None]] = {

}
