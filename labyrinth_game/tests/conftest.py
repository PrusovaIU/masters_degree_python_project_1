from unittest.mock import MagicMock, Mock

import pytest

from labyrinth_game.schemas.game_state import GameState, Player
from labyrinth_game.schemas.room import RoomSchema


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
def mock_room_schema() -> Mock:
    """
    :return: мок RoomSchema.
    """
    mock = Mock(spec=RoomSchema)
    return mock
