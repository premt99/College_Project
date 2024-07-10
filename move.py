class Move:
    def __init__(self, name, type, power, accuracy, category, effect=None):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.effect = effect

    def apply_effect(self, target):
        if self.effect:
            self.effect(target)

class PhysicalMove(Move):
    def __init__(self, name, type, power, accuracy, effect=None):
        super().__init__(name, type, power, accuracy, "Physical", effect)

class SpecialMove(Move):
    def __init__(self, name, type, power, accuracy, effect=None):
        super().__init__(name, type, power, accuracy, "Special", effect)

class Tackle(PhysicalMove):
    def __init__(self):
        super().__init__("Tackle", "Normal", 40, 100)

class Ember(SpecialMove):
    def __init__(self):
        super().__init__("Ember", "Fire", 25, 100)

class WaterGun(SpecialMove):
    def __init__(self):
        super().__init__("Water Gun", "Water", 30, 100)