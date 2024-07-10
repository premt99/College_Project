class Trainer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

def main():
    print("Welcome to Pokémon Go!")
    print("1. Create a new trainer")
    print("2. Load existing trainer")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("You have chosen to create a new trainer!")
        trainer_name = input("Enter your trainer's name: ")
        trainer_location = input("Enter your trainer's location: ")
        new_trainer = Trainer(trainer_name, trainer_location)
        print("Trainer created successfully!")
        print("Name:", new_trainer.name)
        print("Location:", new_trainer.location)

    elif choice == "2":
        print("You have chosen to load an existing trainer!")
        # Add code to load existing trainer here

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()