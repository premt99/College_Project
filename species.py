from move import *

class Pokemon:
    def __init__(self, name, hp, type, moves):
        self.name = name
        self.hp = hp
        self.type = type
        self.moves = moves

class Pidgey(Pokemon):
    def __init__(self):
        super().__init__("Pidgey", 45, "Normal", [tackle])

class Rattata(Pokemon):
    def __init__(self):
        super().__init__("Rattata", 45, "Normal", [tackle, ember])

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", 45, "Water", [tackle, water_gun])

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", 45, "Fire", [ember])

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", 45, "Grass", [tackle, water_gun])