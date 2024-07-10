from pokemon import *
from battle import *

def main():
    print("Welcome to the Pokémon game!")
    print("Choose your starter Pokémon:")
    print("1. Pidgey")
    print("2. Rattata")
    print("3. Squirtle")
    print("4. Charmander")
    print("5. Bulbasaur")

    choice = int(input("Enter the number of your chosen Pokémon: "))

    if choice == 1:
        player_pokemon = Pidgey()
    elif choice == 2:
        player_pokemon = Rattata()
    elif choice == 3:
        player_pokemon = Squirtle()
    elif choice == 4:
        player_pokemon = Charmander()
    elif choice == 5:
        player_pokemon = Bulbasaur()
    else:
        print("Invalid choice. Defaulting to Pidgey.")
        player_pokemon = Pidgey()

    print(f"You chose {player_pokemon.name}!")

    opponent_pokemon = Charmander()  # For now, the opponent is always Charmander

    battle = Battle(player_pokemon, opponent_pokemon)
    battle.start_battle()

if __name__ == "__main__":
    main()