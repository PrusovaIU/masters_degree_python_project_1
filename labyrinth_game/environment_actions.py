from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.schemas.room import RoomSchema
from labyrinth_game.utils import pseudo_random
from labyrinth_game.constants.item import Items
from labyrinth_game.trap_handler import trigger_trap
from labyrinth_game.constants.trap import Traps


def _find_coin(game_state: GameState) -> None:
    """
    Функция для обнаружения золотой монетки.

    :param game_state: текущее состояние игры.
    :return: None.
    """
    game_state.player.inventory.append(Items.gold_coin)
    print(f"Вам улыбнулась удача! Вы нашли золотой монетку.")


def _fright(game_state: GameState) -> None:
    """
    Функция для испытания страха.

    :param game_state: текущее состояние игры.
    :return: None.
    """
    if Items.sword in game_state.player.inventory:
        print(f"Слабые шорохи доносятся из глубины коридора, будто что-то "
              f"наблюдает за вами. Как только вы берете в руки "
              f"{Items.sword.value}, звуки исчезают, и вокруг снова царит "
              f"безмолвие — словно оружие прогнало невидимых наблюдателей.")
    else:
        trigger_trap(game_state, Traps.ghost)


def _trap(game_state: GameState) -> None:
    """
    Функция для срабатывания ловушки.

    :param game_state: текущее состояние игры.
    :return: None.
    """
    current_room: RoomSchema = get_room(game_state)
    if current_room.trap and Items.torch not in game_state.player.inventory:
        traps = list(Traps)
        trap_id: int = pseudo_random(game_state.steps_taken, len(traps))
        trigger_trap(game_state, traps[trap_id])


def random_event(game_state: GameState) -> None:
    """
    Рандомное событие.

    :param game_state: текущее состояние игры.
    :return: None.
    """
    is_action: int = pseudo_random(game_state.steps_taken, 3)
    match is_action:
        case 1:
            _find_coin(game_state)
        case 2:
            _fright(game_state)
        case 3:
            _trap(game_state)
