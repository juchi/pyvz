
class Wave:
    def __init__(self):
        self.enemies = []

    def get_enemy(self):
        return Enemy()

    def next_enemy_timeout(self):
        return 3000


class Enemy:
    def __init__(self):
        self.life = 100
        self.position = -1, -1
        self.row = -1
