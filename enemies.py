import pygame


class Wave:
    def __init__(self):
        self.enemies = []
        self.enemy_attributes = {'life': 100, 'speed': float(40)/1000}

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
        self.animation_timer = 0
        self.animation_sprite = 0
        self.sprites = []

        for k in range(1, 7):
            sprite = self.get_sprite_surface('./sprites/zombie/Walk' + str(k) + '.png', 50)
            self.sprites.append(sprite)

    def get_sprite_surface(self, img_path, cell_width):
        sprite = pygame.image.load(img_path)
        img_size = sprite.get_size()
        ratio = float(img_size[0]) / img_size[1]
        if ratio > 1:
            width = cell_width
            height = int(width / ratio)
        else:
            height = cell_width
            width = int(height * ratio)

        sprite = pygame.transform.flip(sprite, True, False)
        return pygame.transform.scale(sprite, (width, height))

    def update(self, elapsed_time):
        if self.alive:
            self.position = (self.position[0] - elapsed_time * self.speed, self.position[1])
            self.animation_timer += elapsed_time
            if self.animation_timer >= 300:
                self.animation_timer -= 300
                self.animation_sprite += 1

    def get_sprite(self):
        if len(self.sprites) > 0:
            return self.sprites[self.animation_sprite % len(self.sprites)]
        else:
            return None

    def take_damages(self, damages):
        self.life -= damages
        if self.life < 0:
            self.life = 0
            self.alive = False
