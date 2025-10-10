from enum import Enum


class Items(Enum):
    torch = "torch"
    rusty_key = "rusty_key"
    ancient_book = "ancient_book"
    sword = "sword"
    bronze_box = "bronze_box"
    treasure_chest = "treasure_chest"
    treasure_key = "treasure_key"
    broken_mirror_piece = "broken_mirror_piece"
    illusion_key = "illusion_key"
    old_chain = "old_chain"
    bloodied_key = "bloodied_key"
    iron_hook = "iron_hook"
    broken_shackles = "broken_shackles"
    gold_coin = "gold_coin"


BIG_ITEMS = [
    Items.treasure_chest,
    Items.old_chain
]


Inventory = list[Items]


def add_item_to_inventory(item: Items, inventory: Inventory) -> bool:
    """
    Фукнция добавления предмета в инвентарь.

    :param item: предмет.
    :param inventory: инвентарь.
    :return: true, если предмет добавлен. Иначе false.
    """
    if item in BIG_ITEMS:
        print("Слишком большой предмет. Не влезет в инвентарь.")
        result = False
    else:
        print("Вы подняли: " + item.value)
        inventory.append(item)
        result = True
    return result
