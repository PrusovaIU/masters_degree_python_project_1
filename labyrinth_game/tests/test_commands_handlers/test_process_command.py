from collections.abc import Generator

import pytest
from unittest.mock import patch, Mock
from labyrinth_game import player_actions
from labyrinth_game.constants.command import Commands
from labyrinth_game.constants.direction import Directions
from labyrinth_game.schemas.game_state import GameState
from labyrinth_game import commands_handlers
from contextlib import contextmanager


@pytest.fixture
def mock_game_state() -> Mock:
    return Mock(name="game_state", spec=GameState)


@contextmanager
def patch_commands_handlers(
        object_name: str,
        handlers: dict[str, Mock]
) -> Generator[None, None, None]:
    """
    Патч хандлеров команд.

    :param object_name: имя объекта, который нужно патчить.
    :param handlers: список хандлеров.
    :return: None.
    """
    old = getattr(commands_handlers, object_name)
    try:
        setattr(commands_handlers, object_name, handlers)
        yield None
    finally:
        setattr(commands_handlers, object_name, old)


@pytest.mark.parametrize("command, args, handlers_name", [
    pytest.param(
        Commands.exit,
        None,
        "SIMPLE_COMMANDS_HANDLERS",
        id="simple_command"
    ),
    pytest.param(Commands.go,"args", "COMMAND_HANDLERS", id="command")
])
def test_command(
        mock_game_state: Mock,
        command: Commands,
        args: str | None,
        handlers_name: str
):
    """
    Тест корректных комманд.

    :param mock_game_state: мок состояния игры.
    :param command: команда.
    :params args: аргументы команды.
    :params handlers_name: имя хандлеров команд.
    :return: None.
    """
    handler_mock = Mock(name="handler")
    handlers = {command.value: handler_mock}
    input_str = f"{command.value} {args}" if args else command.value
    with patch_commands_handlers(handlers_name, handlers):
        commands_handlers.process_command(mock_game_state, input_str)
        handler_mock.assert_called_once()


@pytest.mark.parametrize("command", [
    pytest.param(Commands.go, id="go"),
    pytest.param(Commands.use, id="use"),
    pytest.param(Commands.take, id="take")
])
def test_command_without_object(
        mock_game_state: Mock,
        command: Commands
) -> None:
    """
    Тест команд без указания объекта.

    :param mock_game_state: мок состояния игры.
    :param command: команда.
    :return: None.
    """
    from labyrinth_game.commands_handlers import process_command
    with pytest.raises(ValueError):
        process_command(mock_game_state, command.value)


def test_invalid_command(mock_game_state: Mock):
    """
    Тест невалидных команд.

    :param mock_game_state: мок состояния игры.
    :return: None.
    """
    with pytest.raises(ValueError):
        commands_handlers.process_command(
            mock_game_state,
            "invalid_command"
        )
