from collections.abc import Generator

import pytest
from unittest.mock import patch, Mock
from labyrinth_game import player_actions


@pytest.fixture
def mock_solve_puzzle() -> Generator[Mock, None, None]:
    """
    Патч для функции solve_puzzle.

    :return: мок.
    """
    with patch.object(player_actions, 'solve_puzzle') as mock:
        yield mock


def test_solve_puzzle_with_puzzle(
        mock_game_state: Mock,
        mock_solve_puzzle: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock
) -> None:
    """
    Тест решения загадки, когда загадка есть.

    :param mock_game_state: мок состояния игры.
    :param mock_solve_puzzle: мок функции solve_puzzle.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    mock_room_schema.puzzle = ("test_puzzle", "answer", None)
    mock_get_room.return_value = mock_room_schema

    player_actions.solve(mock_game_state)
    mock_solve_puzzle.assert_called_once()


def test_solve_puzzle_withou_puzzle(
        mock_game_state: Mock,
        mock_solve_puzzle: Mock,
        mock_get_room: Mock,
        mock_room_schema: Mock
) -> None:
    """
    Тест решения загадки, когда загадки нет.

    :param mock_game_state: мок состояния игры.
    :param mock_solve_puzzle: мок функции solve_puzzle.
    :param mock_get_room: мок функции get_room.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    mock_room_schema.puzzle = None
    mock_get_room.return_value = mock_room_schema

    player_actions.solve(mock_game_state)
    mock_solve_puzzle.assert_not_called()
