from enum import Enum

from labyrinth_game.constants.direction import Directions


class Commands(Enum):
    """
    Список команд
    """
    look_around = "look_around"
    inventory = "inventory"
    solve = "solve"
    go = "go"
    use = "use"
    take = "take"
    exit = "exit"
    help = "help"


# описание команд
COMMANDS_HELP = {
    Commands.look_around.value: "Осмотреться",
    Commands.inventory.value: "Показать инвентарь",
    Commands.solve.value: "Решить загадку",
    f"{Commands.go.value} <direction>": "Переместиться в указанную комнату",
    f"{Commands.use.value} <object>": "Использовать предмет",
    f"{Commands.take.value} <object>": "Взять предмет",
    Directions.north.value: "Переместиться на север",
    Directions.south.value: "Переместиться на юг",
    Directions.west.value: "Переместиться на запад",
    Directions.east.value: "Переместиться на восток",
    Directions.up.value: "Переместиться вверх",
    Directions.down.value: "Переместиться вниз",
    Commands.exit.value: "Выход из игры"
}
