import pytest
from unittest.mock import Mock
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.item_use_handlers import _use_treasure_key
from labyrinth_game.constants.room import Rooms


def test_use_treasure_key_not_in_treasure_room(
        mock_game_state: GameState
) -> None:
    """
    Тест, что при использовании ключа не в комнате с сокровищами, игра не
    заканчивается.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.current_room = Rooms.entrance
    mock_game_state.game_over = False
    _use_treasure_key(mock_game_state)
    assert not mock_game_state.game_over


def test_use_treasure_key_in_treasure_room(
        mock_game_state: GameState
) -> None:
    """
    Тест, что при использовании ключа в комнате с сокровищами, игра
    заканчивается.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.current_room = Rooms.treasure_room
    _use_treasure_key(mock_game_state)
    assert mock_game_state
