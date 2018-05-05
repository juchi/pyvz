
class State:
    def __init__(self):
        self.stack = None

    def set_stack(self, stack):
        self.stack = stack

    def key_pressed(self, key):
        return

    def update(self, elapsed):
        return

    def mouse_clicked(self, button, pos):
        return


class StateStack:
    def __init__(self):
        self.list = []

    def push(self, state):
        state.set_stack(self)
        self.list.append(state)

    def pop(self):
        if len(self.list) > 0:
            del self.list[len(self.list) - 1]

    def current(self):
        if len(self.list) == 0:
            return None
        return self.list[len(self.list) - 1]
