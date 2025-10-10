from typing import NamedTuple
from .item import Items


class Puzzle(NamedTuple):
    text: str
    answer: str
    prize: Items | None
