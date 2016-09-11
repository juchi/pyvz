import plant
from pygame import Rect
import pygame


class PlantPanel:
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.plants = plant.type_map

    def mouse_clicked(self, pos):
        relative_pos = (pos[0] - self.rect[0], pos[1] - self.rect[1])
        print relative_pos

    def is_point_inside(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        screen.fill((100, 100, 100), self.rect)
        i = 0
        for key, p in self.plants.iteritems():
            rect = Rect(0, i * self.rect.width, self.rect.width, self.rect.width)
            rect.move_ip(self.rect.topleft)
            screen.fill(p["color"], rect)
            if self.game.current_plant_type == key:
                pygame.draw.rect(screen, (255, 0, 0), rect, 1)
            i += 1
