from labyrinth_game.schemas.puzzle import Puzzle
from labyrinth_game.solve_puzzle import solve_puzzle
from unittest.mock import patch
from collections.abc import Generator
from unittest.mock import Mock, patch
from labyrinth_game.constants.item import Items
import pytest


@pytest.fixture
def input_mock() -> Generator[Mock, None, None]:
    with patch("builtins.input") as mock:
        yield mock


@pytest.mark.parametrize("prize", [
    pytest.param(Items.gold_coin, id="prize_is_gold"),
    pytest.param(None, id="prize_is_none"),
])
@pytest.mark.parametrize("answer", [
    pytest.param("1", id="answer_is_integer"),
    pytest.param("one", id="answer_is_string"),
])
def test_solve_puzzle_correct_answer_with_prize(
        prize: Items | None,
        answer: str,
        input_mock: Mock,
) -> None:
    """
    Тест правильного ответа.
    :param prize: приз за загадку.
    :param answer: ответ.
    :param input_mock: мок функции input.
    :return: None.
    """
    puzzle = Puzzle(text="text", answer=("1", "one"), prize=prize)
    input_mock.return_value = answer
    result, result_prize = solve_puzzle(puzzle)
    assert result is True
    assert result_prize == prize


def test_solve_puzzle_incorrect_answer(
        input_mock: Mock
) -> None:
    """
    Тест неправильного ответа.
    :param input_mock: мок функции input.
    :return: None.
    """
    puzzle = Puzzle(text="text", answer=("answer",), prize=Items.gold_coin)
    input_mock.return_value = "incorrect"
    result, prize = solve_puzzle(puzzle)
    assert result is False
    assert prize is None
