import pytest
from labyrinth_game.inventory import (Inventory, add_item_to_inventory,
                                      BIG_ITEMS)
from labyrinth_game.constants.item import Items


@pytest.mark.parametrize("inventory", [
    pytest.param([], id="empty_inventory"),
    pytest.param([Items.treasure_chest], id="non_empty_inventory")
])
def test_add_item_to_inventory_success(inventory: Inventory) -> None:
    """
    Тест успешного добавления маленького предмета в инвентарь.

    :param inventory: инвентарь.
    :return: None.
    """
    added_item = Items.gold_coin
    assert added_item not in inventory
    res = add_item_to_inventory(added_item, inventory)
    assert res
    assert added_item in inventory


def test_add_item_to_inventory_big_item() -> None:
    """
    Тест, что нельзя добавить большой предмет в инвентарь.

    :return: None.
    """
    added_item = BIG_ITEMS[0]
    inventory = []
    res = add_item_to_inventory(added_item, inventory)
    assert not res
    assert added_item not in inventory
