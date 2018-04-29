import pygame


class PauseState:
    def __init__(self, screen, config):
        self.stack = None
        self.screen = screen
        (w, h) = screen.get_size()
        self.rect = pygame.Rect(w / 4, h / 4, w / 2, h / 2)

    def set_stack(self, stack):
        self.stack = stack

    def update(self, elapsed):
        self.screen.fill((220, 220, 220), self.rect)

        default_font = pygame.font.get_default_font()
        title_font = pygame.font.Font(default_font, 20)
        text_surface = title_font.render("Pause", True, (0, 0, 0))
        self.screen.blit(text_surface, (self.rect.left, self.rect.top))

    def mouse_clicked(self, button, pos):
        return

    def key_pressed(self, key):
        if key == pygame.K_ESCAPE:
            self.stack.pop()
        return

