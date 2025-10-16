from labyrinth_game import trap_handler
from unittest.mock import Mock
from labyrinth_game.constants.item import Items
from labyrinth_game.tests.conftest import mock_pseudo_random


def test_inventory_lost_from_empty_inventory(
        mock_game_state: Mock,
        mock_pseudo_random: Mock
) -> None:
    """
    Тест проверяет, что при пустом инвентаре ничего не происходит.

    :param mock_game_state: мок состояния игры.
    :param mock_pseudo_random: мок функции pseudo_random.
    :return: None.
    """
    mock_game_state.player.inventory = []
    trap_handler._inventory_lost(mock_game_state)
    mock_pseudo_random.assert_not_called()


def test_inventory_lost_from_not_empty_inventory(
        mock_game_state: Mock,
        mock_pseudo_random: Mock
) -> None:
    """
    Тест проверяет, что при не пустом инвентаре происходит потеря предмета.

    :param mock_game_state: мок состояния игры.
    :param mock_pseudo_random: мок функции pseudo_random.
    :return: None.
    """
    mock_game_state.player.inventory = [Items.gold_coin, Items.rusty_key]
    mock_pseudo_random.return_value = 0

    trap_handler._inventory_lost(mock_game_state)

    mock_pseudo_random.assert_called_once()
    assert mock_game_state.player.inventory == [Items.rusty_key]
