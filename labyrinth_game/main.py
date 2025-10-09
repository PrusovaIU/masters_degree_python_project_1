#!/usr/bin/env python3
from labyrinth_game.schemas.game_state import GameState, initial_state
from labyrinth_game.utils import describe_current_room


def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    game_state: GameState = initial_state()
    while not game_state.game_over:
        describe_current_room(game_state)

    print("Лабиринт будет ждать вас снова!")



if __name__ == '__main__':
    main()