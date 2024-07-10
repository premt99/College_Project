import random
from battle import battle
from moves import Move, PhysicalMove, SpecialMove

class Pokemon:
    def __init__(self, name, type, hp, moves=None):
        self.name = name
        self.type = type
        self.hp = hp
        self.moves = moves if moves else []

class Trainer:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.pokemon_list = []

def encounter_pokemon(trainer):
    pokemon_species = ["Pidgey", "Rattata", "Squirtle", "Charmander", "Bulbasaur"]
    pokemon_type = ["Normal", "Fire", "Water", "Grass"]
    pokemon_hp = random.randint(10, 50)

    if random.choice(pokemon_species) == "Pidgey":
        moves = [PhysicalMove("Tackle", "Normal", 40, 100)]
    elif random.choice(pokemon_species) == "Rattata":
        moves = [PhysicalMove("Tackle", "Normal", 40, 100), SpecialMove("Ember", "Fire", 25, 100)]
    elif random.choice(pokemon_species) == "Squirtle":
        moves = [PhysicalMove("Tackle", "Normal", 40, 100), SpecialMove("Water Gun", "Water", 30, 100)]
    elif random.choice(pokemon_species) == "Charmander":
        moves = [SpecialMove("Ember", "Fire", 25, 100)]
    elif random.choice(pokemon_species) == "Bulbasaur":
        moves = [PhysicalMove("Tackle", "Normal", 40, 100), SpecialMove("Water Gun", "Water", 30, 100)]

    pokemon = Pokemon(random.choice(pokemon_species), random.choice(pokemon_type), pokemon_hp, moves)

    print(f"A wild {pokemon.name} has appeared!")
    print(f"Type: {pokemon.type}, HP: {pokemon.hp}")

    choice = input("Do you want to catch it? (y/n): ")

    if choice.lower() == "y":
        battle(trainer, pokemon)  # Call the battle function
        if pokemon.hp <= 0:
            print("You've caught the Pokémon!")
            trainer.pokemon_list.append(pokemon)
            print(f"{trainer.name}'s Pokémon list: {[p.name for p in trainer.pokemon_list]}")
        else:
            print("You've failed to catch the Pokémon!")
    else:
        print("You've run away!")

def main():
    trainer_name = input("Enter your trainer name: ")
    trainer = Trainer(trainer_name)

    while True:
        print("\n1. Explore the wild")
        print("2. View Pokémon list")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            encounter_pokemon(trainer)
        elif choice == "2":
            print(f"{trainer.name}'s Pokémon list: {[p.name for p in trainer.pokemon_list]}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()