#!python3 -i

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import src.Patterns as Patterns
import src.UserInput as UserInput
import atexit



def help():
    funcs = \
"""
off(): turns the dome off (solid black)
solid(color): turns the dome a solid color (number 0 <= n <= 255)
patloop(): loop through random patterns
exit(): quits the program
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


args = UserInput.UserInput()
patterns = Patterns.Patterns(device=args.get_output(), numch=120, tickrate=1000)

# Doesn't work...
def shutdown():
    patterns.shutdown()

# Stop pattern observables when exiting
atexit.register(patterns.shutdown)

# Print help text
help()


