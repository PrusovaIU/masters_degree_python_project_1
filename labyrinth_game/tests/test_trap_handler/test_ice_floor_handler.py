from unittest.mock import Mock

from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.trap_handler import _icy_floor_handler


def test_icy_floor_handler_only_injury(
        mock_game_state: Mock,
        mock_get_injury: Mock,
        mock_inventory_lost: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock
):
    """
    Тест функции в случае, когда игрок получает только рану, но ничего не
    теряет.

    :param mock_game_state: мок состояния игры.
    :param mock_get_injury: мок функции _get_injury.
    :param mock_inventory_lost: мок функции _inventory_lost.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    mock_game_state.current_room = Rooms.entrance
    mock_game_state.player.hp = 10

    mock_get_room.return_value = mock_room_schema
    mock_inventory_lost.return_value = None
    mock_room_schema.items = []
    mock_get_injury.return_value = 3

    _icy_floor_handler(mock_game_state)

    mock_get_injury.assert_called_once()
    mock_inventory_lost.assert_called_once()
    mock_get_room.assert_not_called()

    assert not mock_room_schema.items


def test_icy_floor_handler_with_lost_item(
        mock_game_state: Mock,
        mock_get_injury: Mock,
        mock_inventory_lost: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock
) -> None:
    """
    Тест функции в случае, когда игрок теряет предмет.

    :param mock_game_state: мок состояния игры.
    :param mock_get_injury: мок функции _get_injury.
    :param mock_inventory_lost: мок функции _inventory_lost.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    mock_game_state.current_room = Rooms.entrance
    mock_game_state.player.hp = 10

    item = Items.rusty_key
    mock_get_room.return_value = mock_room_schema
    mock_room_schema.items = []
    mock_get_injury.return_value = 3
    mock_inventory_lost.return_value = item

    _icy_floor_handler(mock_game_state)

    mock_get_injury.assert_called_once()
    mock_inventory_lost.assert_called_once()
    mock_get_room.assert_called_once()

    assert item in mock_room_schema.items
