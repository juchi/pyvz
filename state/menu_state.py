import gui
from level import Level
from level_select_state import LevelSelectState
from state import State


class MenuState(State):
    def __init__(self, screen, core):
        State.__init__(self)
        self.core = core

        self.gui = gui.Window(screen, screen.get_rect())
        self.gui.background_color = (255, 255, 255)
        ng_btn = gui.Button("New game", (50, 50, 120, 30))
        ng_btn.set_onclick_callback(self.new_game)
        level_btn = gui.Button("Select level", (200, 50, 120, 30))
        level_btn.set_onclick_callback(lambda: self.stack.push(LevelSelectState(screen, self.core)))
        exit_btn = gui.Button("Exit", (50, 90, 120, 30))
        exit_btn.set_onclick_callback(lambda: self.stack.pop())
        self.gui.add_child(ng_btn)
        self.gui.add_child(level_btn)
        self.gui.add_child(exit_btn)

    def new_game(self):
        game_state = self.core.create_game()
        self.stack.push(game_state)
        level = Level(self.core.config["levels"][0])
        game_state.new_game(level)

    def update(self, elapsed):
        self.gui.render()
        return

    def mouse_clicked(self, button, pos):
        self.gui.mouse_clicked(button, pos)
        return
