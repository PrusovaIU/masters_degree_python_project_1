from unittest.mock import MagicMock, Mock, patch
from collections.abc import Generator

import pytest

from labyrinth_game.schemas.game_state import GameState, Player
from labyrinth_game import environment_actions


@pytest.fixture
def mock_game_state() -> MagicMock:
    """
    :return: мок состояния игры.
    """
    game_state = MagicMock(spec=GameState)
    game_state.player = MagicMock(spec=Player)
    game_state.player.inventory = []
    return game_state


@pytest.fixture
def mock_trigger_trap() -> Generator[Mock, None, None]:
    """
    Патч функции trigger_trap.

    :return: мок.
    """
    with patch.object(environment_actions, "trigger_trap") as mock:
        yield mock
