from enum import Enum
from functools import partial
from typing import Any, Callable

from labyrinth_game import player_actions
from labyrinth_game.constants.command import COMMANDS_HELP, Commands
from labyrinth_game.constants.direction import Directions
from labyrinth_game.schemas.game_state import GameState


def _help(_: GameState) -> None:
    print("Доступные команды:")
    for command, description in COMMANDS_HELP.items():
        print(f"\t{command} - {description}")


def _commands_handlers(
        handlers: dict[Enum, Callable[[GameState], None]]
) -> dict[str, Callable[[GameState], None]]:
    return {command.value: handler for command, handler in handlers.items()}


SIMPLE_COMMANDS_HANDLERS: dict[str, Callable[[GameState], None]] = _commands_handlers({
    Commands.exit: player_actions.game_exit,
    Commands.look_around: player_actions.look_around,
    Commands.inventory: player_actions.show_inventory,
    Commands.solve: player_actions.solve,
    Commands.help: _help,
    **{
        direction: partial(player_actions.move, direction_name=direction.value)
        for direction in Directions
    }
})
COMMAND_HANDLERS: dict[str, Callable[[GameState, Any], None]] = _commands_handlers({
    Commands.go: player_actions.move,
    Commands.use: player_actions.use,
    Commands.solve: player_actions.solve,
    Commands.take: player_actions.take,
})


def process_command(game_state: GameState, command: str) -> None:
    """
    Обработка команды.

    :param game_state: состояние игры.
    :param command: команда.
    :return: None.

    :raises ValueError: если команда не распознана.
    """
    command, _, args = command.partition(" ")
    if command in SIMPLE_COMMANDS_HANDLERS:
        command_handler: Callable[[GameState], None] = \
            SIMPLE_COMMANDS_HANDLERS[command]
        command_handler(game_state)
    elif not args:
        print(f"Укажите объект. Например, {Commands.use.value} coin")
    elif command in COMMAND_HANDLERS:
        args = args.strip().lower()
        command_handler: Callable[[GameState, Any], None] = \
            COMMAND_HANDLERS[command]
        command_handler(game_state, args)
    else:
        raise ValueError("Unknown command")


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
