#!python3 -i

import UserInput as UserInput
import Patterns as Patterns
import sys
import atexit


def help():
    funcs = \
"""Functions:

off(): turns the dome off (solid black)
solid(color): turns the dome a solid color (number 0 <= n <= 255)
patloop(): loop through random patterns

"""
    print(funcs)

def off():
    patterns.solid(0, 0, 0)

def solid(r, g, b):
    r = _get_ranged_int(r, 0, 255)
    g = _get_ranged_int(g, 0, 255)
    b = _get_ranged_int(b, 0, 255)
    if r != None and g != None and b != None:
        patterns.solid(r, g, b)

def _get_ranged_int(x, low, high):
    try:
        x = int(x)
        if x < low:
            x = low
        elif x > high:
            x = high
        return x
    except TypeError:
        print("Invalid value:", x)
        return None

def patloop():
    patterns.start()


userinput = UserInput.UserInput()
patterns = Patterns.Patterns(device='/dev/null', numchannels=120, tickrate=1000)

# Doesn't work...
def shutdown():
    patterns.shutdown()

# Stop pattern observables when exiting
atexit.register(patterns.shutdown)

# Print help text
help()


