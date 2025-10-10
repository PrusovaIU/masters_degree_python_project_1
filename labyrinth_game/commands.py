from enum import Enum
from typing import Callable, Any

from labyrinth_game.player_actions import exit, show_inventory, \
    solve, move, use
from labyrinth_game.schemas.game_state import GameState


class Commands(Enum):
    inventory = "inventory"
    solve = "solve"
    go = "go"
    use = "use"
    exit = "exit"


SIMPLE_COMMANDS_HANDLERS: dict[Commands, Callable[[GameState], None]] = {
    Commands.exit: exit,
    Commands.inventory: show_inventory,
    Commands.solve: solve
}
COMMAND_HANDLERS: dict[Commands, Callable[[GameState, Any], None]] = {
    Commands.go: move,
    Commands.use: use,
    Commands.solve: solve,
}


def process_command(game_state: GameState, command: str) -> None:
    """
    Обработка команды.

    :param game_state: состояние игры.
    :param command: команда.
    :return: None.
    """
    command, _, args = command.partition(" ")
    command = Commands(command)
    if command in SIMPLE_COMMANDS_HANDLERS:
        command_handler: Callable[[GameState], None] = \
            SIMPLE_COMMANDS_HANDLERS[command]
        command_handler(game_state)
    elif not args:
        print(f"Укажите объект. Например, {command.value} coin")
    else:
        args = args.strip().lower()
        command_handler: Callable[[GameState, Any], None] = \
            COMMAND_HANDLERS[command]
        command_handler(game_state, args)


def get_input(game_state: GameState, promt: str="> ") -> None:
    """
    Функция для получения ввода пользователя.

    :param game_state: текущее состояние игры.
    :param promt: строка с просьбой ввести команду.
    :return: None.
    """
    try:
        result = False
        while not result:
            command = input(promt)
            if command:
                process_command(game_state, command)
                result = True
    except ValueError:
        print("Некорректная команда")
    except KeyError:
        print("Команда не реализована. Обратитесь к разработчику.")
