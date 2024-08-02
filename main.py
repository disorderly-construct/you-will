import sys
import time

# Flag to control whether input is accepted
accepting_input = True

# Function to type out text with a delay between characters
def typewriter_effect(text, delay=0.05):
    global accepting_input
    accepting_input = False  # Disable input
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    accepting_input = True  # Enable input

# Function to handle player choices with input control
def get_player_choice(choices):
    while True:
        if accepting_input:
            choice = input("> ").strip().lower()
            if choice in choices:
                return choice
            else:
                typewriter_effect("Invalid choice. Try again.")
        else:
            time.sleep(0.1)  # Wait for a short period before checking again

# Tutorial function
def tutorial():
    typewriter_effect("You will take part in a predominantly text-based game.")
    typewriter_effect("You will be give n a scenario and options to choose from.")
    typewriter_effect("You will type in the field your selection and enter f to continue.\n")
    typewriter_effect("You will be given a scenario with specific target values. You will not overshoot these values.\n")

# Main game function
def main():
    # Get player name
    player_name = input("What is your name? ")
    typewriter_effect(f"Welcome to my game, {player_name}")
    
    # Ask if the player wants to go through the tutorial
    yn_tutorial = input("Would you like to go through the tutorial? (y/n) ").strip().lower()
    if yn_tutorial == "y":
        tutorial()
    
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
