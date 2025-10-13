import pytest
from labyrinth_game import environment_actions
from labyrinth_game.schemas.game_state import GameState, Player
from labyrinth_game.constants.item import Items
from labyrinth_game.constants.trap import Traps
from unittest.mock import MagicMock, patch, Mock
from collections.abc import Generator


@pytest.fixture
def mock_get_room() -> Generator[Mock, None, None]:
    with patch.object(environment_actions, "get_room") as mock_get_room:
        yield mock_get_room


def test_trap_with_torch_in_inventory_does_nothing(
        mock_game_state: MagicMock,
        mock_get_room: Mock,
        mock_trigger_trap: Mock
):
    """
    Тест для проверки, что при наличии факела в инвентаре, ловушка не
    инициируется.
    
    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок метода get_room.
    :param mock_trigger_trap: мок метода trigger_trap.
    :return: None.
    """
    mock_game_state.player.inventory = [Items.torch]
    environment_actions._trap(mock_game_state)

    mock_get_room.assert_called_once()
    mock_trigger_trap.assert_not_called()


@pytest.fixture
def mock_pseudo_random() -> Generator[Mock, None, None]:
    """
    Патч для функции pseudo_random.

    :return: мок.
    """
    with patch.object(environment_actions, "pseudo_random") as mock:
        yield mock


def test_trap_without_torch_and_room_has_trap(
        mock_game_state: MagicMock,
        mock_get_room: Mock,
        mock_pseudo_random: Mock,
        mock_trigger_trap: Mock
):
    """
    Тест для проверки, что при отсутствии факела в инвентаре и наличии ловушки
    в комнате инициируется ловушка.

    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок метода get_room.
    :param mock_pseudo_random: мок метода pseudo_random.
    :param mock_trigger_trap: мок метода trigger_trap.
    :return: None.
    """
    mock_game_state.player.inventory = []

    current_room = MagicMock()
    current_room.trap = True
    mock_get_room.return_value = current_room

    mock_pseudo_random.return_value=1

    environment_actions._trap(mock_game_state)

    mock_get_room.assert_called_once()
    mock_pseudo_random.assert_called_once()
    mock_trigger_trap.assert_called_once()


def test_trap_without_torch_and_room_has_no_trap(
        mock_game_state: MagicMock,
        mock_get_room: Mock,
        mock_pseudo_random: Mock,
        mock_trigger_trap: Mock
):
    """
    Тест для проверки, что при отсутствии ловушки в комнате, ловушка не
    инициируется.

    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок метода get_room.
    :param mock_pseudo_random: мок метода pseudo_random.
    :param mock_trigger_trap: мок метода trigger_trap.
    :return:
    """
    mock_game_state.player.inventory = []

    current_room = MagicMock()
    current_room.trap = False

    mock_get_room.return_value=current_room

    environment_actions._trap(mock_game_state)

    mock_get_room.assert_called_once()
    # Проверяем, что pseudo_random и trigger_trap не вызывались
    mock_pseudo_random.assert_not_called()
    mock_trigger_trap.assert_not_called()
