# input_handler.py
import time
from typewriter import typewriter_effect, accepting_input

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
