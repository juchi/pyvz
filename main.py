import sys, pygame, yaml
from game_state import GameState


def main():
    pygame.init()
    pygame.font.init()

    config_file = file('config.yml', 'r')
    config_data = yaml.load(config_file)

    size = 800, 600
    screen = pygame.display.set_mode(size)

    state = GameState(screen, config_data)
    state.new_game()

    old_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        elapsed = current_time - old_time
        old_time = current_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                state.mouse_clicked(event.button, pygame.mouse.get_pos())
            if event.type == pygame.KEYUP:
                state.key_pressed(event.key)

        state.update(elapsed)
        pygame.display.flip()

main()
