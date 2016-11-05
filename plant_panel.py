from pygame import Rect
import pygame


class PlantPanel:
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.buttons = self.construct_buttons()

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
            screen.fill(button.plant_type.color, button.rect.move(self.rect.topleft))
            if self.game.current_plant_type == button.plant_type:
                pygame.draw.rect(screen, (255, 0, 0), button.rect.move(self.rect.topleft), 1)


class Button:
    def __init__(self, rect, ptype):
        self.rect = rect
        self.plant_type = ptype
