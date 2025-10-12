from enum import Enum


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
