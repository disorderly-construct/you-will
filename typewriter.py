# typewriter.py
import sys
import time

# Flag to control whether input is accepted
accepting_input = True

def typewriter_effect(text, delay=0.05):
    global accepting_input
    accepting_input = False  # Disable input
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    accepting_input = True  # Enable input
