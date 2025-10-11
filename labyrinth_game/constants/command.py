from enum import Enum


class Commands(Enum):
    """
    Список команд
    """
    inventory = "inventory"
    solve = "solve"
    go = "go"
    use = "use"
    take = "take"
    exit = "exit"
    help = "help"
