class Wave:
    def __init__(self, enemy_factory):
        self.enemies = []
        self.enemy_count = 0
        self.enemy_created = 0
        self.enemy_delay = 1000
        self.enemy_factory = enemy_factory
        self.enemy_attributes = {'life': 100, 'speed': float(40)/1000}

    def get_enemy(self):
        if self.enemy_created >= self.enemy_count:
            return None

        self.enemy_created += 1
        return self.enemy_factory.new_enemy(self.enemy_attributes)

    def next_enemy_timeout(self):
        return self.enemy_delay


class EnemyFactory:
    def __init__(self, sprite_loader):
        self.sprite_loader = sprite_loader
        return

    def new_enemy(self, attributes):
        sprites = self.sprite_loader.load_animation('zombie', 'Walk', True)
        enemy = Enemy(attributes, sprites)
        return enemy


class Enemy:
    def __init__(self, attributes, sprites):
        self.life = attributes['life']
        self.position = -1, -1
        self.row = -1
        self.speed = attributes['speed']
        self.alive = True
        self.active = True
        self.money_value = 50
        self.animation_timer = 0
        self.animation_sprite = 0
        self.sprites = sprites

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
