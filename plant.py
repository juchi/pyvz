
type_map = {
    1: {"color": (0, 255, 0), "power": 30, "life": 50, "range": 400},
    2: {"color": (0, 196, 0), "power": 40, "life": 50, "range": 400},
    3: {"color": (0, 128, 0), "power": 50, "life": 50, "range": 400}
}


class Plant:
    def __init__(self, type, grid_position, grid, game):
        self.type = type
        type_data = type_map[type]
        self.color = type_data["color"]
        self.life = type_data["life"]
        self.grid_position = grid_position
        self.position = grid.get_pixel_coords(grid_position)
        self.grid = grid
        self.game = game
        self.power = type_data["power"]
        self.base_fire_cooldown = 1000
        self.fire_cooldown = self.base_fire_cooldown
        self.range = type_data["range"]
        self.bullet_speed = float(300)/1000

    def update(self, elapsed_time):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= elapsed_time
            return

        enemy = self.grid.find_enemy_in_range(self.position, self.range)
        if enemy is not None:
            self.fire()

    def fire(self):
        self.fire_cooldown = self.base_fire_cooldown
        bullet = Bullet(self.grid.get_pixel_coords(self.grid_position), self.bullet_speed, self.power)
        self.game.bullets.append(bullet)


class Bullet:
    def __init__(self, position, speed, power):
        self.position = position
        self.speed = speed
        self.power = power
        self.active = True

    def update(self, elapsed_time):
        if self.active:
            self.position = (self.position[0] + self.speed * elapsed_time, self.position[1])
