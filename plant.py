

class Plant:
    def __init__(self, type, position, grid, game):
        self.type = type
        self.life = 100
        self.position = position
        self.grid = grid
        self.game = game
        self.power = 30
        self.base_fire_cooldown = 1000
        self.fire_cooldown = self.base_fire_cooldown
        self.range = 10
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
        bullet = Bullet(self.position, self.bullet_speed, self.power)
        self.game.bullets.append(bullet)


class Bullet:
    def __init__(self, position, speed, power):
        self.position = position
        self.speed = speed
        self.power = power

    def update(self, elapsed_time):
        self.position = (self.position[0] + self.speed * elapsed_time, self.position[1])
