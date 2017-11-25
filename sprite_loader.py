import pygame, os


class SpriteLoader:
    def __init__(self, cell_width):
        self.cell_width = cell_width
        return

    def load_animation(self, entity_name, animation_name):
        sprites = []
        basename = './sprites/' + entity_name + '/' + animation_name
        extension = '.png'

        index = 1
        while True:
            filename = basename + str(index) + extension
            if not os.path.exists(filename):
                break
            sprite = self.get_sprite_surface(filename, self.cell_width)
            sprites.append(sprite)
            index += 1

        return sprites

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