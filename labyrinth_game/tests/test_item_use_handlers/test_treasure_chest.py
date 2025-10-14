import pytest
from unittest.mock import Mock, patch
from labyrinth_game.schemas.game_state import GameState
from collections.abc import Generator
from labyrinth_game import item_use_handlers
from labyrinth_game.constants.item import Items


@pytest.fixture
def mock_use_treasure_key() -> Generator[Mock, None, None]:
    """
    Патч функции _use_treasure_key.

    :return: мок.
    """
    with patch.object(item_use_handlers, "_use_treasure_key") as mock:
        yield mock


def test_use_treasure_chest_with_key(
        mock_game_state: GameState,
        mock_use_treasure_key: Mock
) -> None:
    """
    Тест использования сундука с ключом.

    :param mock_game_state: мок состояния игры.
    :param mock_use_treasure_key: мок функции _use_treasure_key.
    :return: None.
    """
    mock_game_state.player.inventory.append(Items.treasure_key)
    item_use_handlers._use_treasure_key(mock_game_state)
    mock_use_treasure_key.assert_called_once()


@pytest.fixture
def mock_hack_treasure_chest() -> Generator[Mock, None, None]:
    """
    Патч функции _hack_treasure_chest.

    :return: мок.
    """
    with patch.object(item_use_handlers, "_hack_treasure_chest") as mock:
        yield mock


def test_use_treasure_chest_hacking_success(
        mock_game_state: GameState,
        mock_hack_treasure_chest: Mock
) -> None:
    """
    Тест использования сундука без ключа.

    :param mock_game_state: мок состояния игры.
    :param mock_hack_treasure_chest: мок функции _hack_treasure_chest.
    :return: None.
    """
    item_use_handlers._use_treasure_chest(mock_game_state)
    mock_hack_treasure_chest.assert_called_once()
