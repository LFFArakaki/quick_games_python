class Game:
    def __init__(self, name, difficulties):
        self._name = name
        self.difficulties = difficulties
    def __str__(self):
        return self._name