import pytest
from unittest.mock import patch, Mock
from collections.abc import Generator
from labyrinth_game import player_actions
from labyrinth_game.constants.item import Items


@pytest.fixture
def mock_add_item_to_inventory() -> Generator[Mock, None, None]:
    """
    Патч функции add_item_to_inventory.

    :return: мок.
    """
    with patch.object(player_actions, 'add_item_to_inventory') as mock:
        yield mock


@pytest.mark.parametrize("success", [
    pytest.param(True, id="success"),
    pytest.param(False, id="fail")
])
def test_take(
        mock_game_state: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock,
        mock_add_item_to_inventory: Mock,
        success: bool
) -> None:
    """
    Тест успешного выполнения действия take.

    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :param mock_add_item_to_inventory: мок функции add_item_to_inventory.
    :return:
    """
    mock_room_schema.items = [Items.gold_coin]
    mock_get_room.return_value = mock_room_schema
    mock_add_item_to_inventory.return_value = success

    player_actions.take(mock_game_state, Items.gold_coin.value)

    assert (Items.gold_coin in mock_room_schema.items) is not success


def test_take_unknown_object(
        mock_game_state: Mock,
        mock_get_room: Mock
) -> None:
    """
    Тест выполнения действия take с неизвестным объектом.

    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок функции get_room.
    :return:
    """
    player_actions.take(mock_game_state, "test_object")
    mock_get_room.assert_not_called()


def test_take_item_not_in_room(
        mock_game_state: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock,
        mock_add_item_to_inventory: Mock,
) -> None:
    """
    Тест выполнения действия take с предметом, которого нет в комнате.

    :param mock_game_state: мок состояния игры.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :param mock_add_item_to_inventory: мок функции add_item_to_inventory.
    :return:
    """
    mock_room_schema.items = []
    mock_get_room.return_value = mock_room_schema

    player_actions.take(mock_game_state, Items.gold_coin.value)
    mock_add_item_to_inventory.assert_not_called()
