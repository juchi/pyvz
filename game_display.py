import pygame


class GameDisplay:
    def __init__(self, screen):
        self.screen = screen

    def display_grid(self, pos, grid):
        black = 0, 0, 0
        xmax = grid.size[0] + pos[0]
        ymax = grid.size[1] + pos[1]

        for x in range(pos[0], xmax + 1, grid.size[0] / grid.cols):
            pygame.draw.line(self.screen, black, (x, pos[1]), (x, ymax))

        for y in range(pos[1], ymax + 1, grid.size[1] / grid.rows):
            pygame.draw.line(self.screen, black, (pos[0], y), (xmax, y))

    def display_hud(self, player):
        default_font = pygame.font.get_default_font()
        hud_font = pygame.font.Font(default_font, 16)
        money_surface = hud_font.render("Money:" + str(player.money), True, (0, 0, 0))
        self.screen.blit(money_surface, (0, 0))

    def display_plants(self, plants, grid):
        for plant in plants:
            pos = (plant.position[0] + grid.position[0],
                   plant.position[1] + grid.position[1])
            sprite = plant.get_sprite()
            if sprite is not None:
                self.screen.blit(sprite, (pos[0] - sprite.get_width() / 2, pos[1] - sprite.get_height() / 2))
            else:
                pygame.draw.circle(self.screen, plant.color, pos, grid.cellsize / 2)

    def display_enemies(self, enemies, grid):
        for enemy in enemies:
            if not enemy.alive:
                continue
            pos = (enemy.position[0] + grid.position[0],
                   enemy.position[1] + grid.position[1])
            pos = (int(pos[0]), int(pos[1]))
            sprite = enemy.get_sprite()
            if sprite is not None:
                self.screen.blit(sprite, (pos[0] - sprite.get_width()/2, pos[1] - sprite.get_height()/2))
            else:
                pygame.draw.circle(self.screen, (255, 0, 0), pos, grid.cellsize / 2)

    def display_bullets(self, bullets, grid):
        for bullet in bullets:
            if not bullet.active:
                continue
            pos = (bullet.position[0] + grid.position[0],
                   bullet.position[1] + grid.position[1])
            pos = (int(pos[0]), int(pos[1]))
            pygame.draw.circle(self.screen, (255, 0, 0), pos, grid.cellsize / 10)
