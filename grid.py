
class Grid:
    def __init__(self, size, position):
        self.rows = 10
        self.cols = 10
        self.size = size
        self.position = position

    def get_cell_y(self, row):
        cellsize = self.size[0] / self.rows
        return self.position[1] + self.size[1] / cellsize * row

    def get_grid_coords(self, pos):
        cellsize = self.size[0] / self.rows
        if pos[0] < self.position[0] or pos[1] < self.position[1]:
            return -1, -1

        x = (pos[0] - self.position[0]) / cellsize
        y = (pos[1] - self.position[1]) / cellsize

        if x > 9 or y > 9:
            return -1, -1

        return x, y
