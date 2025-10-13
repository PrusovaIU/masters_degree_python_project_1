from labyrinth_game.constants.item import Items
from unittest.mock import MagicMock, patch, Mock
from labyrinth_game.schemas.game_state import GameState, Player
from labyrinth_game import environment_actions
from collections.abc import Generator
import pytest


@pytest.fixture
def mock_print() -> Generator[Mock, None, None]:
    """
    Патч для функции print.

    :return: мок для функции print.
    """
    with patch.object(environment_actions, "print") as mock_print:
        yield mock_print


@pytest.fixture
def mock_game_state() -> MagicMock:
    """
    :return: мок состояния игры.
    """
    game_state = MagicMock(spec=GameState)
    game_state.player = MagicMock(spec=Player)
    game_state.player.inventory = []
    return game_state


def test_fright_with_sword_in_inventory(
        mock_game_state: MagicMock,
        mock_print: Mock
) -> None:
    """
    Тест успешного испытания страха с оружием в инвентаре.

    :param mock_game_state: Мок состояния игры.
    :param mock_print: Мок функции print.
    :return: None.
    """
    mock_game_state.player.inventory.append(Items.sword)
    environment_actions._fright(mock_game_state)
    mock_print.assert_called_once()


def test_fright_without_sword_in_inventory(
        mock_game_state: MagicMock,
        mock_print: Mock
) -> None:
    """
    Тест неуспешного испытания страха без оружия в инвентаре.

    :param mock_game_state: Мок состояния игры.
    :param mock_print: Мок функции print.
    :return: None.
    """
    with patch.object(
            environment_actions, "trigger_trap"
    ) as mock_trap:
        environment_actions._fright(mock_game_state)
        mock_trap.assert_called_once()
        mock_print.assert_not_called()
