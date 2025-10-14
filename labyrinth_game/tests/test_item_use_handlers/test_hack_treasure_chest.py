import pytest
from unittest.mock import Mock, patch
from collections.abc import Generator
from labyrinth_game import item_use_handlers


@pytest.fixture
def mock_user_input() -> Generator[Mock, None, None]:
    """
    Патч функции user_input.

    :return: мок.
    """
    with patch.object(item_use_handlers, "user_input") as mock:
        yield mock


@pytest.fixture
def mock_solve_puzzle() -> Generator[Mock, None, None]:
    """
    Патч функции solve_puzzle.

    :return: мок.
    """
    with patch.object(item_use_handlers, "solve_puzzle") as mock:
        yield mock


@pytest.mark.parametrize("is_hacked", [
    pytest.param(True, id="success"),
    pytest.param(False, id="fail")
])
def test_hack_treasure_chest(
        mock_game_state: Mock,
        mock_user_input: Mock,
        mock_solve_puzzle: Mock,
        is_hacked: bool
) -> None:
    """
    Тест взлома сундука с сокровищами.

    :param mock_game_state: мок состояния игры.
    :param mock_user_input: мок функции user_input.
    :param mock_solve_puzzle: мок функции solve_puzzle.
    :param is_hacked: флаг успешного взлома.
    :return: None.
    """
    mock_game_state.game_over = False
    mock_user_input.return_value = "y"
    mock_solve_puzzle.return_value = is_hacked

    item_use_handlers._hack_treasure_chest(mock_game_state)

    mock_solve_puzzle.assert_called_once()
    mock_solve_puzzle.assert_called_once()
    assert mock_game_state.game_over is is_hacked


def test_hack_treasure_chest_not_hack(
        mock_game_state: Mock,
        mock_user_input: Mock,
        mock_solve_puzzle: Mock
) -> None:
    """
    Тест, что взлом не начат.
    :param mock_game_state: мок состояния игры.
    :param mock_user_input: мок функции user_input.
    :param mock_solve_puzzle: мок функции solve_puzzle.
    :return: None.
    """
    mock_user_input.return_value = "n"
    mock_game_state.game_over = False

    item_use_handlers._hack_treasure_chest(mock_game_state)

    assert mock_game_state.game_over is False
    mock_solve_puzzle.assert_not_called()
