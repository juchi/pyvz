import pygame


class Window:
    def __init__(self, screen, rect):
        self.screen = screen
        self.children = []
        self.rect = rect
        self.surface = screen.subsurface(rect)

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        for child in self.children:
            child.render(self.surface)

    def mouse_clicked(self, button, pos):
        if not self.rect.collidepoint(pos):
            return

        for child in self.children:
            if child.get_rect().move(self.rect.left, self.rect.top).collidepoint(pos):
                child.on_click()


class Button:
    def __init__(self, text="Button", rect=(0, 0, 0, 0)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.on_click_callback = None

    def render(self, surface):
        default_font = pygame.font.get_default_font()
        title_font = pygame.font.Font(default_font, 20)
        text_surface = title_font.render(self.text, True, (0, 0, 0))
        surface.fill((0, 0, 0), self.rect)
        surface.fill((240, 240, 240), self.rect.inflate(-2, -2))
        surface.blit(text_surface, (self.rect.left, self.rect.top))

    def set_onclick_callback(self, callback):
        self.on_click_callback = callback

    def on_click(self):
        if self.on_click_callback:
            self.on_click_callback()

    def get_rect(self):
        return self.rect
