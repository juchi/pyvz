
class PlantType:
    def __init__(self, color, power, life, range, price):
        self.color = tuple(color)
        self.power = power
        self.life = life
        self.range = range
        self.price = price
        self.fire_cooldown = 1000
