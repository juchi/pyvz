
type_map = {
    1: {"color": (0, 255, 0), "power": 30, "life": 50, "range": 400},
    2: {"color": (0, 196, 0), "power": 40, "life": 50, "range": 400},
    3: {"color": (0, 128, 0), "power": 50, "life": 50, "range": 400}
}


class PlantType:
    def __init__(self, color, power, life, range):
        self.color = color
        self.power = power
        self.life = life
        self.range = range
        self.price = 50
