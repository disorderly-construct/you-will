# tutorial.py
import sys
from typewriter import typewriter_effect

def tutorial1():
    typewriter_effect("You will take part in a predominantly text-based game.")
    typewriter_effect("You will be given a scenario and options to choose from.")
    typewriter_effect("You will type in the field your selection and press enter continue.\n")
    typewriter_effect("You will be given a scenario with specific target values. You will not overshoot these values.\n")
    
def tutorial2():
    tutorial2continue = input("Continue? (y/n)")
    if tutorial2continue == "y":
        typewriter_effect("Bring the subject to the required levels without going over. Deviate by 5 or less to cycle. Deviate by 1 or less to succeed.\n")
        typewriter_effect("\nYou will not break the cycle.")
        typewriter_effect("You will keep them alive. You will break them.")
        typewriter_effect("You will.\n")
    else:
        sys.exit("Goodbye")
