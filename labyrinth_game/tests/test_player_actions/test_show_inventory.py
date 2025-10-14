from unittest.mock import Mock
from labyrinth_game.player_actions import show_inventory
from labyrinth_game.constants.item import Items



def test_show_inventory_empty(capfd, mock_game_state: Mock):
    """
    Тестирование вывода пустого инвентаря.

    :param capfd: stdout, stderr.
    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    show_inventory(mock_game_state)
    out, err = capfd.readouterr()
    assert "Инвентарь пуст" in out


def test_show_inventory_not_empty(capfd, mock_game_state: Mock):
    """
    Тестирование вывода не пустого инвентаря.

    :param capfd: stdout, stderr.
    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    mock_game_state.player.inventory = [
        Items.gold_coin,
        Items.gold_coin,
        Items.rusty_key
    ]
    show_inventory(mock_game_state)

    out, err = capfd.readouterr()
    assert "В вашем инвентаре:" in out
    assert f"2 x {Items.gold_coin.value}" in out
    assert f"1 x {Items.rusty_key.value}" in out
