from typing import Optional

import pytest
from unittest.mock import patch, Mock
from collections.abc import Generator
from labyrinth_game import player_actions
from labyrinth_game.schemas.room import RoomSchema
from labyrinth_game.constants.item import Items
from labyrinth_game.exceptions import DeadException


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


@pytest.fixture
def mock_describe_current_room() -> Generator[Mock, None, None]:
    """
    Патч функции describe_current_room.

    :return: мок.
    """
    with patch.object(
            player_actions, "describe_current_room"
    ) as mock:
        yield mock


@pytest.fixture
def mock_random_event() -> Generator[Mock, None, None]:
    """
    Патч функции random_event.

    :return: мок.
    """
    with patch.object(player_actions, "random_event") as mock:
        yield mock

@pytest.mark.parametrize("lock", [
    pytest.param(None, id="no_lock"),
    pytest.param(Items.rusty_key, id="lock")
])
def test_move_success(
        mock_game_state: Mock,
        mock_get_next_room: Mock,
        mock_room_schema: Mock,
        mock_random_event: Mock,
        mock_describe_current_room: Mock,
        lock: Optional[Items]
) -> None:
    """
    Тест успешного входа в комнату.

    :param mock_game_state: мок текущего состояния игры.
    :param mock_get_next_room: мок функции get_next_room.
    :param mock_room_schema: мок RoomSchema.
    :param mock_random_event: мок функции random_event.
    :param mock_describe_current_room: мок функции describe_current_room.
    :param lock: тип ключа.
    :return: None.
    """
    if lock:
        mock_game_state.player.inventory.append(lock)

    mock_room_schema.lock = lock

    mock_game_state.steps_taken = 0
    mock_game_state.player.hp = 10

    room_name = "test_room"
    mock_get_next_room.return_value = (room_name, mock_room_schema)

    player_actions.move(mock_game_state, "north")

    assert mock_game_state.steps_taken == 1
    assert mock_game_state.current_room == room_name

    mock_random_event.assert_called_once()
    mock_describe_current_room.assert_called_once()


def test_move_fail(
        mock_game_state: Mock,
        mock_get_next_room: Mock,
        mock_room_schema: Mock,
        mock_random_event: Mock,
        mock_describe_current_room: Mock
) -> None:
    """
    Тест попытки входа в запертую комнату без ключа.

    :param mock_game_state: мок текущего состояния игры.
    :param mock_get_next_room: мок функции get_next_room.
    :param mock_room_schema: мок RoomSchema.
    :param mock_random_event: мок функции random_event.
    :param mock_describe_current_room: мок функции describe_current_room.
    :return: None.
    """
    mock_room_schema.lock = Items.rusty_key

    room_name = "test_room"
    mock_game_state.current_room = room_name
    mock_game_state.steps_taken = 0
    mock_game_state.player.hp = 10

    mock_get_next_room.return_value = (room_name, mock_room_schema)

    player_actions.move(mock_game_state, "north")

    assert mock_game_state.steps_taken == 0
    assert mock_game_state.current_room == room_name

    mock_random_event.assert_not_called()
    mock_describe_current_room.assert_not_called()


def test_move_fail_hp(
        mock_game_state: Mock,
        mock_get_next_room: Mock,
        mock_room_schema: Mock,
        mock_random_event: Mock,
        mock_describe_current_room: Mock
) -> None:
    """
    Тест обнуления здоровья после рандомного события.

    :param mock_game_state: мок текущего состояния игры.
    :param mock_get_next_room: мок функции get_next_room.
    :param mock_room_schema: мок RoomSchema.
    :param mock_random_event: мок функции random_event.
    :param mock_describe_current_room: мок функции describe_current_room.
    :return: None.
    """
    mock_room_schema.lock = None

    mock_game_state.steps_taken = 0
    mock_game_state.player.hp = 0

    room_name = "test_room"
    mock_get_next_room.return_value = (room_name, mock_room_schema)

    with pytest.raises(DeadException):
        player_actions.move(mock_game_state, "north")

    mock_random_event.assert_called_once()
    mock_describe_current_room.assert_not_called()
