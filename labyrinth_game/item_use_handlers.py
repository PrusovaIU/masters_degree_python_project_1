from collections import UserDict
from typing import Callable

from labyrinth_game.constants.item import Items
from labyrinth_game.constants.room import Rooms
from labyrinth_game.constants.rooms_list import ROOMS
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.schemas.puzzle import solve_puzzle
from labyrinth_game.utils import user_input

UseItemHandlerType = Callable[[GameState], None]


def _use_torch(game_state: GameState) -> None:
    print("Стало светлее.")


def _use_sword(game_state: GameState) -> None:
    print("С мечом в руках Вы чувствуете себя увереннее.")


def _use_bronze_box(game_state: GameState) -> None:
    if Items.rusty_key in game_state.player.inventory:
        new_item = Items.gold_coin
        game_state.player.inventory.append(new_item)
        print(f"Вы открыли бронзовую коробку и нашли: {new_item.value}")
    else:
        print("Бронзовая коробочка заперта.")


def _use_treasure_key(game_state: GameState) -> None:
    if game_state.current_room != Rooms.treasure_room:
        print("Вы осматриваете ключ. Маленький золоченый ключик.")
    else:
        print("Вы вставляете ключ в сундук, проворачиваете его, замок щелкает "
              "и сундук открывается.")
        game_state.game_over = True


def _use_treasure_chest(game_state: GameState) -> None:
    if Items.treasure_key in game_state.player.inventory:
        _use_treasure_key(game_state)
    else:
        print("Вы осматриваете сундук. Старый, но дорого отделанный. "
              "На корпусе виднеется небольшое отверстие для ключа.")
        hacking: str = user_input(
            "Попробовать взломать сундук?", ["y", "n"]
        )
        if hacking == "y":
            puzzle = ROOMS[Rooms.treasure_room].puzzle
            if solve_puzzle(puzzle):
                print("Взлом успешен!")
                game_state.game_over = True
            else:
                print("Взлом не удался.")


def _default_action(game_state: GameState) -> None:
    print("С этим ничего нельзя сделать.")


class ItemHandlers(UserDict[Items, UseItemHandlerType]):
    def __missing__(self, key: Items) -> UseItemHandlerType:
        return _default_action


USE_ITEMS_HANDLERS = ItemHandlers({
    Items.torch: _use_torch,
    Items.sword: _use_sword,
    Items.bronze_box: _use_bronze_box,
    Items.treasure_key: _use_treasure_key,
    Items.treasure_chest: _use_treasure_chest
})
