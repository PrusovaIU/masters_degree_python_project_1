from unittest.mock import Mock
from labyrinth_game.constants.item import Items
from labyrinth_game.item_use_handlers import _use_bronze_box


def test_use_bronze_box_with_rusty_key_in_inventory(
        mock_game_state: Mock
) -> None:
    """
    Тестируем использование бронзовой коробки с ключом в инвентаре.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.player.inventory.append(Items.rusty_key)
    _use_bronze_box(mock_game_state)

    assert Items.rusty_key in mock_game_state.player.inventory
    assert Items.gold_coin in mock_game_state.player.inventory


def test_use_bronze_box_without_rusty_key_in_inventory(
        mock_game_state: Mock
) -> None:
    """
    Тестируем использование бронзовой коробки без ключа в инвентаре.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    assert Items.rusty_key not in mock_game_state.player.inventory
    _use_bronze_box(mock_game_state)
    assert not mock_game_state.player.inventory
