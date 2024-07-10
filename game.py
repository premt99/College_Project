class Pokemon:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", 60, 85, 60)

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 45, 48, 65)

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 39, 52, 43)