import pygame
import random
from player import Player
from plant import Plant
from enemies import *

grid_pos = (50, 20)
grid_size = (400, 400)
cellsize = grid_size[0] / 10


class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.plants = []
        self.current_wave = None
        self.enemies = []
        self.time_since_last_enemy = 0

    def mouse_clicked(self, button, pos):
        if button == 1:
            coords = get_grid_coords(pos)
            if coords[0] != -1 and self.player.money >= 50:
                self.player.money -= 50
                self.plants.append(Plant(1, coords))

    def update(self, elapsed_time):
        self.update_timers(elapsed_time)
        self.update_wave_status()
        display_grid(self.screen, grid_pos, grid_size)
        display_hud(self.screen, self.player)
        display_plants(self.screen, self.plants)
        display_enemies(self.screen, self.enemies)

    def update_timers(self, elapsed_time):
        self.time_since_last_enemy += elapsed_time

    def update_wave_status(self):
        if self.current_wave is None:
            self.current_wave = Wave()
        if self.time_since_last_enemy > self.current_wave.next_enemy_timeout():
            next_enemy = self.current_wave.get_enemy()
            next_enemy.row = random.randint(0, 9)
            next_enemy.position = (550, get_cell_y(next_enemy.row))
            self.enemies.append(next_enemy)
            self.time_since_last_enemy = 0


def display_grid(screen, pos, size):
    screen.fill((255, 255, 255))
    black = 0, 0, 0
    xmax = size[0] + pos[0]
    ymax = size[1] + pos[1]

    for x in range(pos[0], xmax + 1, size[0] / 10):
        pygame.draw.line(screen, black, (x, pos[1]), (x, ymax))

    for y in range(pos[1], ymax + 1, size[1] / 10):
        pygame.draw.line(screen, black, (pos[0], y), (xmax, y))


def get_grid_coords(pos):
    if pos[0] < grid_pos[0] or pos[1] < grid_pos[1]:
        return -1, -1

    x = (pos[0] - grid_pos[0]) / cellsize
    y = (pos[1] - grid_pos[1]) / cellsize

    if x > 9 or y > 9:
        return -1, -1

    return x, y


def get_cell_y(row):
    return grid_pos[1] + grid_size[1] / cellsize * row


def display_hud(screen, player):
    default_font = pygame.font.get_default_font()
    hud_font = pygame.font.Font(default_font, 16)
    money_surface = hud_font.render("Money:" + str(player.money), True, (0, 0, 0))
    screen.blit(money_surface, (0, 0))


def display_plants(screen, plants):
    for plant in plants:
        pos = (plant.position[0] * cellsize + grid_pos[0] + cellsize/2,  plant.position[1] * cellsize + grid_pos[1] + cellsize/2)
        pygame.draw.circle(screen, (0, 255, 0), pos, cellsize / 2)


def display_enemies(screen, enemies):
    for enemy in enemies:
        pos = (enemy.position[0] + grid_pos[0] + cellsize/2,  enemy.row * cellsize + grid_pos[1] + cellsize/2)
        pygame.draw.circle(screen, (255, 0, 0), pos, cellsize / 2)
