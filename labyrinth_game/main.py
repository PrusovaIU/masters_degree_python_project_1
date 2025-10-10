#!/usr/bin/env python3
from labyrinth_game.schemas.game_state import GameState, initial_state
from labyrinth_game.rooms_functional import describe_current_room
from labyrinth_game.commands import get_input
from labyrinth_game.exceptions import ExitException


def main():
    print("Добро пожаловать в Лабиринт сокровищ!\n"
          "Для выхода из игры используйте команду 'exit' или Сtrl+C")
    game_state: GameState = initial_state()
    describe_current_room(game_state)
    try:
        while not game_state.game_over:
            get_input(game_state)
    except (KeyboardInterrupt, EOFError, ExitException):
        print("Выход из игры...", end='')
    else:
        print("Вы выиграли!")
    finally:
        print("Лабиринт будет ждать вас снова!")


if __name__ == '__main__':
    main()