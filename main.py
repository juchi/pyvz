import pygame, yaml

from state.game_state import GameState
from state.menu_state import MenuState
from state.state import StateStack


class Core:
    def __init__(self, screen):
        config_file = file('config.yml', 'r')
        self.config = yaml.load(config_file)
        self.screen = screen

    def create_menu(self):
        return MenuState(self.screen, self)

    def create_game(self):
        return GameState(self.screen, self.config)


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("PyVZ")

    size = 800, 600
    screen = pygame.display.set_mode(size)

    core = Core(screen)

    state_stack = StateStack()
    state_stack.push(core.create_menu())

    game_running = True
    old_time = pygame.time.get_ticks()

    while game_running:
        state = state_stack.current()
        if not state:
            break
        current_time = pygame.time.get_ticks()
        elapsed = current_time - old_time
        old_time = current_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONUP:
                state.mouse_clicked(event.button, pygame.mouse.get_pos())
            if event.type == pygame.KEYUP:
                state.key_pressed(event.key)

        state.update(elapsed)
        pygame.display.flip()

    pygame.quit()

main()
