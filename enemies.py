
class Wave:
    def __init__(self):
        self.enemies = []
        self.enemy_attributes = {'life': 100, 'speed': float(50)/1000}

    def get_enemy(self):
        return Enemy(self.enemy_attributes)

    def next_enemy_timeout(self):
        return 3000


class Enemy:
    def __init__(self, attributes):
        self.life = attributes['life']
        self.position = -1, -1
        self.row = -1
        self.speed = attributes['speed']
        self.alive = True
        self.money_value = 50

    def update(self, elapsed_time):
        if self.alive:
            self.position = (self.position[0] - elapsed_time * self.speed, self.position[1])

    def take_damages(self, damages):
        self.life -= damages
        if self.life < 0:
            self.life = 0
            self.alive = False
