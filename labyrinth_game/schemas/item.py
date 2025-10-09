from collections import UserDict
from enum import Enum
from collections.abc import Callable


class Items(Enum):
    torch = "torch"
    rusty_key = "rusty_key"
    ancient_book = "ancient_book"
    sword = "sword"
    bronze_box = "bronze_box"
    treasure_chest = "treasure_chest"
    broken_mirror_piece = "broken_mirror_piece"
    illusion_key = "illusion_key"
    old_chain = "old_chain"
    bloodied_key = "bloodied_key"
    iron_hook = "iron_hook"
    broken_shackles = "broken_shackles"


Inventory = list[Items]


def _use_torch(inventory: Inventory) -> None:
    print("Стало светлее.")


def _use_sword(inventory: Inventory) -> None:
    print("С мечом в руках Вы чувствуете себя увереннее.")


def _use_bronze_box(inventory: Inventory) -> None:
    if Items.rusty_key in inventory:
        new_item = Items.rusty_key
        inventory.append(new_item)
        print(f"Вы открыли бронзовую коробку и нашли: {new_item.value}")
    else:
        print("Вы открываете бронзовую коробку, но ничего не находите.")

def _default_action(inventory: Inventory) -> None:
    print("С этим ничего нельзя сделать.")


class ItemHandlers(UserDict[Items, Callable[[Inventory], None]]):
    def __missing__(self, key: Items) -> Callable[[Inventory], None]:
        return _default_action


USE_ITEMS_HANDLERS = ItemHandlers({
    Items.torch: _use_torch,
    Items.sword: _use_sword,
    Items.bronze_box: _use_bronze_box
})
