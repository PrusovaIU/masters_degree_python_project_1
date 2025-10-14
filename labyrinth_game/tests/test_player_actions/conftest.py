from typing import Generator
from unittest.mock import Mock, patch

import pytest

from labyrinth_game import player_actions
from labyrinth_game.schemas.room import RoomSchema


@pytest.fixture
def mock_get_room() -> Generator[Mock, None, None]:
    """
    Патч функции get_room.

    :return: мок.
    """
    with patch.object(player_actions, "get_room") as mock:
        yield mock


@pytest.fixture
def mock_get_next_room() -> Generator[Mock, None, None]:
    """
    Патч функции get_next_room.

    :return: мок.
    """
    with patch.object(player_actions, "get_next_room") as mock:
        yield mock


@pytest.fixture
def mock_room_schema() -> Mock:
    """
    :return: мок RoomSchema.
    """
    mock = Mock(spec=RoomSchema)
    return mock
