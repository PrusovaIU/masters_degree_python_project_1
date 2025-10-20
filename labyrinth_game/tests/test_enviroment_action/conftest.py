from unittest.mock import Mock, patch
from collections.abc import Generator

import pytest

from labyrinth_game import environment_actions


@pytest.fixture
def mock_trigger_trap() -> Generator[Mock, None, None]:
    """
    Патч функции trigger_trap.

    :return: мок.
    """
    with patch.object(environment_actions, "trigger_trap") as mock:
        yield mock


@pytest.fixture
def mock_get_room() -> Generator[Mock, None, None]:
    with patch.object(environment_actions, "get_room") as mock_get_room:
        yield mock_get_room
