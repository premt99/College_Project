import random

def battle(trainer, wild_pokemon):
    print(f"\n{trainer.name} is battling a wild {wild_pokemon.name}!")

    while wild_pokemon.hp > 0:
        print(f"\n{wild_pokemon.name}'s HP: {wild_pokemon.hp}")
        print(f"{trainer.name}'s Pokémon list: {[p.name for p in trainer.pokemon_list]}")

        choice = input("Choose a Pokémon to battle with (or 'run' to flee): ")

        if choice.lower() == "run":
            print("You've fled the battle!")
            return

        chosen_pokemon = next((p for p in trainer.pokemon_list if p.name.lower() == choice.lower()), None)

        if chosen_pokemon:
            print(f"\n{chosen_pokemon.name} is battling {wild_pokemon.name}!")

            while chosen_pokemon.hp > 0 and wild_pokemon.hp > 0:
                print(f"\n{chosen_pokemon.name}'s HP: {chosen_pokemon.hp}")
                print(f"{wild_pokemon.name}'s HP: {wild_pokemon.hp}")

                move_choice = input("Choose a move (or 'witch' to switch Pokémon): ")

                if move_choice.lower() == "switch":
                    break

                chosen_move = next((m for m in chosen_pokemon.moves if m.name.lower() == move_choice.lower()), None)

                if chosen_move:
                    print(f"\n{chosen_pokemon.name} uses {chosen_move.name}!")

                    if random.random() < chosen_move.accuracy / 100:
                        damage = chosen_move.power
                        wild_pokemon.hp -= damage
                        print(f"{wild_pokemon.name} takes {damage} damage!")
                    else:
                        print(f"{chosen_pokemon.name} misses!")

                    if wild_pokemon.hp > 0:
                        wild_move = random.choice(wild_pokemon.moves)
                        print(f"\n{wild_pokemon.name} uses {wild_move.name}!")

                        if random.random() < wild_move.accuracy / 100:
                            damage = wild_move.power
                            chosen_pokemon.hp -= damage
                            print(f"{chosen_pokemon.name} takes {damage} damage!")
                        else:
                            print(f"{wild_pokemon.name} misses!")

            if chosen_pokemon.hp <= 0:
                print(f"{chosen_pokemon.name} has fainted!")
                trainer.pokemon_list.remove(chosen_pokemon)
            elif wild_pokemon.hp <= 0:
                print(f"{wild_pokemon.name} has fainted!")
                return
        else:
            print("Invalid Pokémon choice. Try again!")

    if wild_pokemon.hp <= 0:
        print(f"You've caught the {wild_pokemon.name}!")
        trainer.pokemon_list.append(wild_pokemon)
        print(f"{trainer.name}'s Pokémon list: {[p.name for p in trainer.pokemon_list]}")
    else:
        print("You've failed to catch the Pokémon!")