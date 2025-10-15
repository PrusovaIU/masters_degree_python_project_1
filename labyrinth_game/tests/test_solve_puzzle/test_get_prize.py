from unittest.mock import Mock

import pytest
from labyrinth_game.solve_puzzle import _get_prize
from labyrinth_game.constants.room import Rooms
from labyrinth_game.constants.item import Items


def test_get_prize_with_prize(mock_game_state: Mock):
    """
    Тест, когда приз есть, но не находится в комнате сокровищ.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.current_room = Rooms.hall  # Не сундук
    mock_game_state.game_over = False
    prize = Items.treasure_key

    _get_prize(mock_game_state, prize)

    assert prize in mock_game_state.player.inventory
    assert mock_game_state.game_over is False


def test_get_prize_with_prize_in_treasure_room(mock_game_state: Mock):
    """
    Текст, когда приз есть, и игрок находится в комнате сокровищ.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.current_room = Rooms.treasure_room
    mock_game_state.game_over = False
    prize = Items.gold_coin

    _get_prize(mock_game_state, prize)

    assert prize in mock_game_state.player.inventory
    assert mock_game_state.game_over is True


def test_get_prize_with_no_prize(mock_game_state: Mock):
    """
    Тест, когда приза нет.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.current_room = Rooms.hall
    mock_game_state.game_over = False

    _get_prize(mock_game_state, None)

    assert mock_game_state.player.inventory == []
    assert mock_game_state.game_over is False
