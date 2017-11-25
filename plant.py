

class Plant:
    def __init__(self, type, grid_position, grid, game, sprites):
        self.type = type
        self.color = type.color
        self.life = type.life
        self.power = type.power
        self.range = type.range
        self.base_fire_cooldown = type.fire_cooldown
        self.fire_cooldown = self.base_fire_cooldown
        self.bullet_speed = float(300) / 1000
        self.grid_position = grid_position
        self.position = grid.get_pixel_coords(grid_position)
        self.grid = grid
        self.game = game
        self.animation_sprite = 0
        self.animation_timer = 0
        self.sprites = sprites

    def get_sprite(self):
        if len(self.sprites) > 0:
            return self.sprites[self.animation_sprite % len(self.sprites)]
        else:
            return None

    def update(self, elapsed_time):
        self.animation_timer += elapsed_time
        if self.animation_timer >= 300:
            self.animation_timer -= 300
            self.animation_sprite += 1

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


class PlantFactory:
    def __init__(self, sprite_loader, game_state):
        self.sprite_loader = sprite_loader
        self.game_state = game_state
        return

    def new_plant(self, plant_type, coords):
        entity_name = self.get_entity_name(plant_type)
        sprites = self.sprite_loader.load_animation(entity_name, 'idle_', False)
        obj = Plant(plant_type, coords, self.game_state.grid, self.game_state, sprites)
        return obj

    def get_entity_name(self, plant_type):
        if plant_type.name == 'fire':
            return 'wizard_fire'
        if plant_type.name == 'ice':
            return 'wizard_ice'
        else:
            return 'wizard'


class Bullet:
    def __init__(self, position, speed, power):
        self.position = position
        self.speed = speed
        self.power = power
        self.active = True

    def update(self, elapsed_time):
        if self.active:
            self.position = (self.position[0] + self.speed * elapsed_time, self.position[1])
