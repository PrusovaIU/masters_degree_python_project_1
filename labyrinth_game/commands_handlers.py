from typing import Any, Callable

from labyrinth_game.constants.command import Commands
from labyrinth_game.player_actions import (game_exit, move, show_inventory,
                                           solve, take, use)
from labyrinth_game.schemas.game_state import GameState

COMMANDS_HELP = {
    Commands.inventory: "Показать инвентарь",
    Commands.solve: "Решить загадку",
    Commands.go: "Переместиться в указанную комнату",
    Commands.use: "Использовать предмет",
    Commands.take: "Взять предмет",
    Commands.exit: "Выход из игры"
}

def _help(_: GameState) -> None:
    print("Доступные команды:")
    for command, description in COMMANDS_HELP.items():
        print(f"\t{command.value} - {description}")


SIMPLE_COMMANDS_HANDLERS: dict[Commands, Callable[[GameState], None]] = {
    Commands.exit: game_exit,
    Commands.inventory: show_inventory,
    Commands.solve: solve,
    Commands.help: _help
}
COMMAND_HANDLERS: dict[Commands, Callable[[GameState, Any], None]] = {
    Commands.go: move,
    Commands.use: use,
    Commands.solve: solve,
    Commands.take: take
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
        print("Некорректная команда. "
              "Используйте help для получения списка команд.")
    except KeyError:
        print("Команда не реализована. Обратитесь к разработчику.")
