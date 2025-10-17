class Mode:
    def __init__(self, name, rules):
        self._name = name
        self._rules = rules
    def play(self):
        self._rules()
    def __str__(self):
        return self._name