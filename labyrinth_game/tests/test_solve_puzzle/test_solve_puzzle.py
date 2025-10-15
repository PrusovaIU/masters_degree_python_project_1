import pytest
from labyrinth_game import solve_puzzle
from unittest.mock import patch, Mock
from collections.abc import Generator
from labyrinth_game.constants.item import Items


@pytest.fixture
def mock_get_answer() -> Generator[Mock, None, None]:
    """
    Патч для функции _get_answer.

    :return: мок.
    """
    with patch.object(solve_puzzle, "_get_answer") as mock:
        yield mock


@pytest.fixture
def mock_get_prize() -> Generator[Mock, None, None]:
    """
    Патч для функции _get_prize.

    :return: мок.
    """
    with patch.object(solve_puzzle, "_get_prize") as mock:
        yield mock


def test_solve_puzzle_success(
        mock_game_state: Mock,
        mock_get_prize: Mock,
        mock_get_answer: Mock,
        mock_room_schema: Mock
):
    """
    Тест успешного решения загадки.

    :param mock_game_state: мок состояния игры.
    :param mock_get_prize: мок функции _get_prize.
    :param mock_get_answer: мок функции _get_answer.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    prize = Items.treasure_key
    mock_room_schema.puzzle = ("test_puzzle", prize)
    mock_get_answer.return_value = (True, prize)

    solve_puzzle.solve_puzzle(mock_game_state, mock_room_schema)

    mock_get_answer.assert_called_once()
    assert mock_room_schema.puzzle is None
    mock_get_prize.assert_called_once()


def test_solve_puzzle_fail(
        mock_game_state: Mock,
        mock_get_prize: Mock,
        mock_get_answer: Mock,
        mock_room_schema: Mock
):
    """
    Тест провала решения загадки.

    :param mock_game_state: мок состояния игры.
    :param mock_get_prize: мок функции _get_prize.
    :param mock_get_answer: мок функции _get_answer.
    :param mock_room_schema: мок схемы комнаты.
    :return: None.
    """
    mock_room_schema.puzzle = ("test_puzzle", None)
    mock_get_answer.return_value = (False, None)

    solve_puzzle.solve_puzzle(mock_game_state, mock_room_schema)

    mock_get_answer.assert_called_once()
    assert mock_room_schema.puzzle is not None
    mock_get_prize.assert_not_called()
