import pygame

from pause_state import PauseState
from game import Game
from game_display import GameDisplay


class GameState:
    def __init__(self, screen, config):
        self.stack = None
        self.screen = screen
        self.game = Game(config, GameDisplay(screen))

    def set_stack(self, stack):
        self.stack = stack

    def new_game(self):
        self.game.new_game()

    def mouse_clicked(self, button, pos):
        self.game.mouse_clicked(button, pos)

    def key_pressed(self, key):
        if key == pygame.K_ESCAPE:
            self.stack.push(PauseState(self.screen, self))

    def update(self, elapsed_time):
        self.screen.fill((255, 255, 255))
        self.game.update(elapsed_time)
