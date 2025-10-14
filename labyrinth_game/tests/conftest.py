from unittest.mock import MagicMock

import pytest

from labyrinth_game.schemas.game_state import GameState, Player


@pytest.fixture
def mock_game_state() -> MagicMock:
    """
    :return: мок состояния игры.
    """
    game_state = MagicMock(spec=GameState)
    game_state.player = MagicMock(spec=Player)
    game_state.player.inventory = []
    return game_state
