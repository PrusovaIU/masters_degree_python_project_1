from unittest.mock import patch, Mock
from collections.abc import Generator
from labyrinth_game import trap_handler
from pytest import fixture


@fixture
def mock_pseudo_random() -> Generator[Mock, None, None]:
    """
    Патч функции pseudo_random.

    :return: мок.
    """
    with patch.object(trap_handler, "pseudo_random") as mock:
        yield mock


@fixture
def mock_get_injury() -> Generator[Mock, None, None]:
    """
    Мок для функции _get_injury.

    :return: мок.
    """
    with patch.object(trap_handler, "_get_injury") as mock:
        yield mock


@fixture
def mock_inventory_lost() -> Generator[Mock, None, None]:
    """
    Мок для функции _inventory_lost.

    :return: мок.
    """
    with patch.object(trap_handler, "_inventory_lost") as mock:
        yield mock

@fixture
def mock_get_room() -> Generator[Mock, None, None]:
    """
    Патч функции get_room.

    :return: мок
    """
    with patch.object(trap_handler, "get_room") as mock_get_room:
        yield mock_get_room
