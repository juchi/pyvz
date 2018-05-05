import pygame
import random
import geometry

from grid import Grid
from player import Player
from plant import PlantFactory
from plant_panel import PlantPanel
from plant_type import PlantType
from enemies import *
from sprite_loader import SpriteLoader

grid_pos = (50, 20)
grid_size = (500, 500)


class Game:
    def __init__(self, config, display):
        self.config = config
        self.display = display
        self.player = Player()
        self.level = None
        self.level_done = False
        self.plants = []
        self.current_wave = None
        self.wave_index = 0
        self.enemies = []
        self.bullets = []
        self.time_since_last_enemy = 0
        self.current_plant_type = None
        self.grid = Grid(grid_size, grid_pos, self)
        self.plant_types = self.create_plant_types()

        self.plant_panel = PlantPanel(self, display.screen, pygame.Rect(0, 40, 40, 200))
        self.sprite_loader = SpriteLoader(self.grid.cellsize)
        self.enemy_factory = EnemyFactory(self.sprite_loader)
        self.plant_factory = PlantFactory(self.sprite_loader, self)

    def new_game(self, level=None):
        if level is not None:
            self.level = level
        if self.level is None:
            print "No level provided"
            quit()

        self.player = Player()
        self.level_done = False
        self.plants = []
        self.current_wave = None
        self.wave_index = 0
        self.enemies = []
        self.bullets = []
        self.time_since_last_enemy = 0
        self.current_plant_type = None

    def mouse_clicked(self, button, pos):
        if button == 1:
            coords = self.grid.get_grid_coords(pos)
            if coords[0] != -1 and self.current_plant_type is not None and self.player.money >= self.current_plant_type.price:
                if self.grid.is_case_free(coords):
                    self.player.money -= self.current_plant_type.price
                    self.plants.append(self.plant_factory.new_plant(self.current_plant_type, coords))
            elif self.plant_panel.is_point_inside(pos):
                self.plant_panel.mouse_clicked(pos)

    def key_pressed(self, key):
        if key == pygame.K_n:
            self.new_game()

    def create_plant_types(self):
        types = []
        for p in self.config['plants']:
            ptype = PlantType(p["name"], p["color"], p["power"], p["life"], p["range"], p["price"])
            types.append(ptype)
        return types

    def update(self, elapsed_time):
        self.update_timers(elapsed_time)

        if not self.level_done:
            self.update_wave_status()
            self.update_enemies(elapsed_time)
            self.update_plants(elapsed_time)
            self.update_bullets(elapsed_time)

        self.plant_panel.draw()
        self.display.display_grid(grid_pos, self.grid)
        self.display.display_hud(self.player)
        self.display.display_plants(self.plants, self.grid)
        self.display.display_enemies(self.enemies, self.grid)
        self.display.display_bullets(self.bullets, self.grid)

    def update_timers(self, elapsed_time):
        self.time_since_last_enemy += elapsed_time

    def update_wave_status(self):
        if self.current_wave is None:
            if self.wave_index < len(self.level.waves):
                wave = Wave(self.enemy_factory)
                wave.enemy_count = self.level.waves[self.wave_index]["enemies"]
                self.wave_index += 1
                self.current_wave = wave
        if self.current_wave and self.time_since_last_enemy > self.current_wave.next_enemy_timeout():
            next_enemy = self.current_wave.get_enemy()
            if next_enemy is None:
                self.current_wave = None
            else:
                next_enemy.row = random.randint(0, 9)
                next_enemy.position = (self.grid.size[0], self.grid.get_center_cell_y(next_enemy.row))
                self.enemies.append(next_enemy)
                self.time_since_last_enemy = 0

    def update_enemies(self, elapsed_time):
        for obj in self.enemies:
            obj.update(elapsed_time)
            if not obj.alive:
                self.player.money += obj.money_value
        self.enemies = [e for e in self.enemies if e.alive]
        if not self.current_wave and len(self.enemies) == 0:
            self.level_done = True

    def update_plants(self, elapsed_time):
        for obj in self.plants:
            obj.update(elapsed_time)

    def update_bullets(self, elapsed_time):
        self.bullets = [b for b in self.bullets if b.active]
        for obj in self.bullets:
            obj.update(elapsed_time)
            for enemy in self.enemies:
                if enemy.alive and geometry.distance(obj.position, enemy.position) < 30:
                    obj.active = False
                    enemy.take_damages(obj.power)
                    if not enemy.alive:
                        self.player.money += 30
                    break
