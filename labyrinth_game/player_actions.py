from labyrinth_game.schemas.game_state import GameState


def show_inventory(game_state: GameState) -> None:
    """
    Функция для вывода в консоль информации об объектах в инвентаре игрока.

    :param game_state: текущее состояние игры
    :return: None
    """
    if game_state.player.inventory:
        objects = "\n\t".join(game_state.player.inventory)
        print(f"В вашем иневентаре:{objects}\n")
    else:
        print("Инвентарь пуст")
