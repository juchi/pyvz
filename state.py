
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
        return self.list[len(self.list) - 1]