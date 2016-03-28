#!python3 -i

import UserInput as UserInput
import Patterns as Patterns
import sys


def help():
    funcs = \
"""Functions:

off(): turns the dome off (solid black)
solid(color): turns the dome a solid color (number 0 <= n <= 255)
patloop(): loop through random patterns

"""
    print(funcs)

def off():
    patterns.solid(0)

def solid(color):
    try:
        color = int(color)
        if color < 0:
            color = 0
        elif color > 255:
            color = 255

        patterns.solid(color)
    except TypeError:
        print("Invalid color")

def patloop():
    patterns.start()


userinput = UserInput.UserInput()
patterns = Patterns.Patterns(numchannels=40, tickrate=30)

# Print help text
help()
