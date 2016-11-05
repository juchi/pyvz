from pygame import Rect
import pygame


class PlantPanel:
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.buttons = self.construct_buttons()

        default_font = pygame.font.get_default_font()
        self.price_font = pygame.font.Font(default_font, 12)

    def construct_buttons(self):
        buttons = []
        i = 0
        for p in self.game.plant_types:
            rect = Rect(0, i * self.rect.width, self.rect.width, self.rect.width)
            buttons.append(Button(rect, p))
            i += 1
        return buttons

    def mouse_clicked(self, pos):
        relative_pos = (pos[0] - self.rect[0], pos[1] - self.rect[1])
        for button in self.buttons:
            if button.rect.collidepoint(relative_pos):
                self.game.current_plant_type = button.plant_type
                break

    def is_point_inside(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        screen.fill((100, 100, 100), self.rect)
        for button in self.buttons:
            button.draw(screen, self.price_font, self.rect.topleft, self.game.current_plant_type == button.plant_type)


class Button:
    def __init__(self, rect, ptype):
        self.rect = rect
        self.plant_type = ptype

    def draw(self, screen, price_font, panel_top_left, selected):
        screen.fill(self.plant_type.color, self.rect.move(panel_top_left))
        price_surface = price_font.render(str(self.plant_type.price), True, (0, 0, 0))
        screen.blit(price_surface, self.rect.move(panel_top_left))
        if selected:
            pygame.draw.rect(screen, (255, 0, 0), self.rect.move(panel_top_left), 1)
