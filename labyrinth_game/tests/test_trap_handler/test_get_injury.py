from unittest.mock import Mock

from labyrinth_game.trap_handler import _get_injury


def test_get_injury(
        mock_game_state: Mock,
        mock_pseudo_random: Mock
) -> None:
    """
    Тестирование функции _get_injury.

    :param mock_game_state: мок состояния игры.
    :param mock_pseudo_random: мок функции pseudo_random.
    :return: None.
    """
    mock_game_state.player.hp = 20
    mock_pseudo_random.return_value = 5

    _get_injury(mock_game_state, 1)

    assert mock_game_state.player.hp == 15
