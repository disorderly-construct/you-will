# main.py
from typewriter import typewriter_effect
from input_handler import get_player_choice
from tutorial import tutorial

def main():
    # Get player name
    player_name = input("What is your name? ")
    typewriter_effect(f"Welcome to my game, {player_name}!")
    
    # Ask if the player wants to go through the tutorial
    yn_tutorial = input("Would you like to go through the tutorial? (y/n) ").strip().lower()
    if yn_tutorial == "y":
        tutorial()
    elif yn_tutorial == "n":
        pass
    elif yn_tutorial not in ["y", "n"]:
        typewriter_effect("Aren't you fuckin' special, eh?")
        # exit() doesnt work yet
    
    # Main game loop
    typewriter_effect("You find yourself in a dark forest. What will you do?")
    
    while True:
        typewriter_effect("Choices: [explore, rest, quit]")
        choice = get_player_choice(["explore", "rest", "quit"])
        
        if choice == "explore":
            typewriter_effect("You venture deeper into the forest...")
            # Add more exploration logic here
        elif choice == "rest":
            typewriter_effect("You decide to rest and regain your strength...")
            # Add rest logic here
        elif choice == "quit":
            typewriter_effect("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
