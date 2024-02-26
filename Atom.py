class Atom:
    def __init__(self, name):
        self.name = name
        self.inverted = False

    def invert(self):
        self.inverted = not self.inverted

    def __str__(self):
        if self.inverted:
            return f'-{self.name}'
        else:
            return self.name
