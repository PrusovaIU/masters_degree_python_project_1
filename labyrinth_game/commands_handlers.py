from typing import Any, Callable

from labyrinth_game import player_actions
from labyrinth_game.constants.command import Commands
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game.constants.direction import Directions
from functools import partial


COMMANDS_HELP = {
    Commands.look_around: "Осмотреться",
    Commands.inventory: "Показать инвентарь",
    Commands.solve: "Решить загадку",
    Commands.go: "Переместиться в указанную комнату",
    Commands.use: "Использовать предмет",
    Commands.take: "Взять предмет",
    Commands.exit: "Выход из игры",
    Directions.north: "Переместиться на север",
    Directions.south: "Переместиться на юг",
    Directions.west: "Переместиться на запад",
    Directions.east: "Переместиться на восток",
    Directions.up: "Переместиться вверх",
    Directions.down: "Переместиться вниз"
}


def _help(_: GameState) -> None:
    print("Доступные команды:")
    for command, description in COMMANDS_HELP.items():
        print(f"\t{command.value} - {description}")


SIMPLE_COMMANDS_HANDLERS: dict[Commands | Directions, Callable[[GameState], None]] = {
    Commands.exit: player_actions.game_exit,
    Commands.look_around: player_actions.look_around,
    Commands.inventory: player_actions.show_inventory,
    Commands.solve: player_actions.solve,
    Commands.help: _help,
    **{
        direction: partial(player_actions.move, direction_name=direction.value)
        for direction in Directions
    }
}
COMMAND_HANDLERS: dict[Commands, Callable[[GameState, Any], None]] = {
    Commands.go: player_actions.move,
    Commands.use: player_actions.use,
    Commands.solve: player_actions.solve,
    Commands.take: player_actions.take,
}


def process_command(game_state: GameState, command: str) -> None:
    """
    Обработка команды.

    :param game_state: состояние игры.
    :param command: команда.
    :return: None.
    """
    command, _, args = command.partition(" ")
    command = Commands(command) \
        if command in list(Commands) \
        else Directions(command)
    if command in SIMPLE_COMMANDS_HANDLERS:
        command_handler: Callable[[GameState], None] = \
            SIMPLE_COMMANDS_HANDLERS[command]
        command_handler(game_state)
    elif not args:
        print(f"Укажите объект. Например, {Commands.use.value} coin")
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
