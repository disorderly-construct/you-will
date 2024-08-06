# main.py
import sys

from input_handler import get_player_choice
from tutorial import tutorial1, tutorial2
from typewriter import typewriter_effect


def main():
    # Get player name
    player_name = input("What is your name? ")
    typewriter_effect(f"Welcome to You Will, {player_name}.\n")
    typewriter_effect("This game will include graphic depictions of violence and lack of humanity. \n If at any time you wish to stop the experience, type 'stop'.")
    
    # Ask if the player wants to go through the tutorial
    yn_tutorial = input("Would you like to go through the tutorial? (y/n) \n").strip().lower()
    if yn_tutorial == "y":
        tutorial1()
        tutorial2()
    elif yn_tutorial == "n":
        pass
    elif yn_tutorial not in ["y", "n"]:
        typewriter_effect("No.")
        sys.exit("Goodbye")
    
    # Main game loop
    typewriter_effect("")
    # someone mumbles at the start as you meet the player, host, and authority figure. severely blackening room focusing in around player and host who has brown sack hood
    # AF: You will begin now, {player_name}.}
    # UI comes up, with categories of torture
    # Unsure of what may come
    # What have i done to bring this down on me
    # There is nothing to attain
    
    
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
