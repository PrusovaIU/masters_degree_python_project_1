from collections.abc import Callable
from time import time_ns

from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.constants.rooms_list import ROOMS
from labyrinth_game.constants.trap import Traps
from labyrinth_game.schemas.game_state import GameState, get_room
from labyrinth_game.schemas.room import RoomSchema
from labyrinth_game.utils import pseudo_random


def _inventory_lost(game_state: GameState) -> Items | None:
    """
    Функция, которая выбирает случайный предмет из инвентаря игрока и удаляет
    его из списка, имитируя потерю предмета из инвентаря.

    :param game_state: состояние игры.
    :return: предмет, который был удалён из инвентаря.
    """
    item: Items | None = None
    if game_state.player.inventory:
        item_id: int = pseudo_random(
            time_ns(),
            len(game_state.player.inventory)
        )
        item = game_state.player.inventory.pop(item_id)
    return item


def _get_injury(game_state: GameState, modulo: int) -> int:
    """
    Функция, которая выбирает случайное количество потерянных единиц здоровья.

    :param game_state: текующее состояние игры.
    :return: количество потерянных единиц здоровья.
    """
    lost_hp: int = pseudo_random(time_ns(), modulo)
    game_state.player.hp -= lost_hp
    return lost_hp


def _icy_floor_handler(game_state: GameState) -> None:
    """
    Функция, которая обрабатывает ловушку "Ледяной пол".
    :param game_state: состояние игры.
    :return: None.
    """
    lost_hp: int = _get_injury(game_state, 3)
    lost_item: Items | None = _inventory_lost(game_state)
    info = (f"В потемках вы не заметили скользкого льда под ногами — "
            f"в следующее мгновение вы потеряли равновесие и резко ударились "
            f"головой о пол.\n"
            f"\tВы потеряли {lost_hp} единиц здоровья. "
            f"Текущее здоровье: {game_state.player.hp}")
    if lost_item:
        info += f"\n\tИз вашей сумки выпал {lost_item.value}"
        current_room: RoomSchema = get_room(game_state)
        current_room.items.append(lost_item)
    print(info)


def _poison_dart_handler(game_state: GameState) -> None:
    """
    Функция, которая обрабатывает ловушку "Ядовитый дротик".

    :param game_state: текущее состояние игры.
    :return: None.
    """
    lost_hp: int = _get_injury(game_state, 5)
    print(f"Внезапно из стены с шипением вылетел пучок ядовитых дротиков — "
          f"время замедлилось, пока они летели прямо к вам.\n"
          f"\tВы потеряли {lost_hp} единиц здоровья. "
          f"Текущее здоровье: {game_state.player.hp}")


def _slime_pit_handler(game_state: GameState) -> None:
    """
    Функция, которая обрабатывает ловушку "Яма слизи".

    :param game_state: текущее состояние игры.
    :return: None.
    """
    lost_hp: int = _get_injury(game_state, 2)
    lost_item: Items | None = _inventory_lost(game_state)
    info = (f"Вы оступились, и в следующее мгновение — беззвучно и внезапно — "
            f"провалились в яму, заполненную липкой, холодной слизью.\n"
            f"\tВы потеряли {lost_hp} единиц здоровья. "
            f"Текущее здоровье: {game_state.player.hp}")
    if lost_item:
        info += (f"\n\tПока Вы выбирались из вязкой слизи, из Вышей сумки "
                 f"выпало {lost_item.value}")
    print(info)


def _ghost_handler(game_state: GameState) -> None:
    """
    Функция, которая обрабатывает ловушку "Призрак".

    :param game_state: текущее состояние игры.
    :return: None.
    """
    lost_item: Items | None = _inventory_lost(game_state)
    info = (f"Из стены неожиданно вышел призрак — его глаза сверкали, а "
            f"голос эхом раздался в голове.\n"
            f"Поддавшись ужасу, вы бросились в бегство, не заботясь о "
            f"направлении.")
    if lost_item:
        info += f"\n\tПока Вы бежали, из Вышей сумки выпало {lost_item.value}"
    rooms = [
        room for room in Rooms
        if room != game_state.current_room and not ROOMS[room].lock
    ]
    room_id: int = pseudo_random(time_ns(), len(rooms))
    game_state.current_room = rooms[room_id]
    print(info)


def _lost_trap_handler(game_state: GameState) -> None:
    print("Внезапно в стене раздалось глухое щелчание... Вы напряглись, "
          "ожидая худшего. Проходит минута, две... Ничего не происходит. "
          "Кажется, ловушка давно вышла из строя.")


TrapHandlerType = Callable[[GameState], None]


_TRAPS_HANDLERS: dict[Traps, TrapHandlerType] = {
    Traps.icy_floor: _icy_floor_handler,
    Traps.poison_dart: _poison_dart_handler,
    Traps.slime_pit: _slime_pit_handler,
    Traps.ghost: _ghost_handler,
    Traps.lost_trap: _lost_trap_handler
}


def trigger_trap(game_state: GameState, trap: Traps) -> None:
    """
    Функция, которая вызывает обработчик ловушки.

    :param game_state: текущее состояние игры.
    :param trap: ловушка.
    :return: None.
    """
    handler: TrapHandlerType = _TRAPS_HANDLERS.get(trap, _lost_trap_handler)
    handler(game_state)
