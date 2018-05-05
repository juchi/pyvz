import pygame
import gui
from state import State


class PauseState(State):
    def __init__(self, screen, game):
        State.__init__(self)
        self.game = game
        self.screen = screen
        (w, h) = screen.get_size()
        self.rect = pygame.Rect(w / 4, h / 4, w / 2, h / 2)

        self.gui = gui.Window(screen, self.rect)
        ng_button = gui.Button("New game", pygame.Rect(10, 50, 120, 30))
        ng_button.set_onclick_callback(lambda: self.game.new_game() or self.stack.pop())
        resume_button = gui.Button("Resume", pygame.Rect(10, 90, 120, 30))
        resume_button.set_onclick_callback(lambda: self.stack.pop())
        quit_button = gui.Button("Quit game", pygame.Rect(10, 130, 120, 30))
        quit_button.set_onclick_callback(lambda: self.stack.pop() or self.stack.pop())
        self.gui.add_child(ng_button)
        self.gui.add_child(resume_button)
        self.gui.add_child(quit_button)

    def update(self, elapsed):
        self.screen.fill((220, 220, 220), self.rect)

        default_font = pygame.font.get_default_font()
        title_font = pygame.font.Font(default_font, 20)
        text_surface = title_font.render("Pause", True, (0, 0, 0))
        self.screen.blit(text_surface, (self.rect.left, self.rect.top))

        self.gui.render()

    def mouse_clicked(self, button, pos):
        self.gui.mouse_clicked(button, pos)
        return

    def key_pressed(self, key):
        if key == pygame.K_ESCAPE and self.stack:
            self.stack.pop()
        return

