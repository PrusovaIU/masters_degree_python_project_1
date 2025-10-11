from labyrinth_game.constants.item import Items

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
