# main.py
import sys
from typewriter import typewriter_effect
from input_handler import get_player_choice
from tutorial import tutorial1
from tutorial import tutorial2

def main():
    # Get player name
    player_name = input("What is your name? ")
    typewriter_effect(f"Welcome to the game, {player_name}.")
    
    # Ask if the player wants to go through the tutorial
    yn_tutorial = input("Would you like to go through the tutorial? (y/n) ").strip().lower()
    if yn_tutorial == "y":
        tutorial1()
        tutorial2()
    elif yn_tutorial == "n":
        pass
    elif yn_tutorial not in ["y", "n"]:
        typewriter_effect("Aren't you fuckin' special, eh?")
        sys.exit("Goodbye")
    
    # Main game loop
    typewriter_effect("You find yourself in a dark, cold stone cell. The exit door is hardly attached. You've gotta be committed. You're in a dungeon, after all. Unsure how you got here, but you feel a sense of purpose.\n")
    typewriter_effect("You see a heavy, marred wodden door in front of you. You move through.\n")
    
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
