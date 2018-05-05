import gui
from level import Level


class LevelSelectState:
    def __init__(self, screen, core):
        self.config = core.config
        self.core = core
        self.stack = None
        self.gui = gui.Window(screen, screen.get_rect())
        self.gui.background_color = (255, 255, 255)

        x = 50
        y = 50
        for index, level in enumerate(self.config["levels"]):
            level_btn = gui.Button("Level " + str(index), (x, y, 120, 30))
            level_btn.set_onclick_callback(lambda : self.select_level(index))
            x += 150
            self.gui.add_child(level_btn)

        back_btn = gui.Button("Back", (50, 130, 120, 30))
        back_btn.set_onclick_callback(lambda: self.stack.pop())
        self.gui.add_child(back_btn)

    def set_stack(self, stack):
        self.stack = stack

    def update(self, elapsed):
        self.gui.render()
        return

    def mouse_clicked(self, button, pos):
        self.gui.mouse_clicked(button, pos)
        return

    def key_pressed(self, key):
        return

    def select_level(self, index):
        level = Level(self.config["levels"][index])
        self.stack.pop()
        game_state = self.core.create_game()
        game_state.new_game(level)
        self.stack.push(game_state)