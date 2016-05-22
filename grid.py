import geometry


class Grid:
    def __init__(self, size, position, game):
        self.rows = 10
        self.cols = 10
        self.size = size
        self.position = position
        self.game = game
        self.cellsize = self.size[1] / self.rows

    def get_cell_y(self, row):
        return self.position[1] + self.cellsize * row

    def get_grid_coords(self, pos):
        if pos[0] < self.position[0] or pos[1] < self.position[1]:
            return -1, -1

        x = (pos[0] - self.position[0]) / self.cellsize
        y = (pos[1] - self.position[1]) / self.cellsize

        if x > 9 or y > 9:
            return -1, -1

        return x, y

    def get_pixel_coords(self, grid_coord):
        x = grid_coord[0] * self.cellsize + self.cellsize/2
        y = grid_coord[1] * self.cellsize + self.cellsize/2
        return x, y

    def find_enemy_in_range(self, position, range):
        for enemy in self.game.enemies:
            if enemy.alive and geometry.delta_y(position, enemy.position) < 20 and geometry.distance(position, enemy.position) < range:
                return enemy

        return None
