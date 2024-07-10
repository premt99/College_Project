import random

class Pokemon:
    def __init__(self, name, type, health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.level = level
        self.experience = experience
        self.moves = moves
        self.is_wild = is_wild

    def attack(self, opponent):
        # Calculate damage based on types and stats
        damage = self.attack * self.level / opponent.defense
        opponent.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.faint()

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
        self.special_attack += 5
        self.special_defense += 5
        self.speed += 5
        print(f"{self.name} has leveled up to level {self.level}!")

    def learn_move(self, move):
        self.moves.append(move)

    def get_stat(self, stat):
        return getattr(self, stat)

class FirePokemon(Pokemon):
    def __init__(self, name, health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild):
        super().__init__(name, "Fire", health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild)

class WaterPokemon(Pokemon):
    def __init__(self, name, health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild):
        super().__init__(name, "Water", health, attack, defense, special_attack, special_defense, speed, level, experience, moves, is_wild)