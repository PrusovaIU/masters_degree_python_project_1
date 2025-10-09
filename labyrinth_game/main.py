#!/usr/bin/env python3
from labyrinth_game.schemas.game_state import GameState, initial_state
from labyrinth_game.utils import describe_current_room
from labyrinth_game.player_actions import get_input


def main():
    print("Добро пожаловать в Лабиринт сокровищ!\n"
          "Для выхода из игры используйте команду 'exit' или Сtrl+C")
    game_state: GameState = initial_state()
    describe_current_room(game_state)
    while not game_state.game_over:
        get_input(game_state)
    print("Лабиринт будет ждать вас снова!")


if __name__ == '__main__':
    main()