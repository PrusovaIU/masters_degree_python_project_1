from typing import NamedTuple

from labyrinth_game.constants.item import Items


class Puzzle(NamedTuple):
    text: str
    answer: tuple[str, ...]
    prize: Items | None
