import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src.Player as Player
import src.Output as output
import src.pattern.FullRandom as full_random
import src.pattern.Tsunami as tsunami
import src.pattern.Sarlacc as sarlacc
from src.UserInput import UserInput

user_input = UserInput()

pattern_makers = [
    lambda: (full_random.get_observable(), 'Full Random Test'),
    lambda: (tsunami.get_observable(), 'Tsunami'),
    lambda: (sarlacc.get_observable(), 'Sarlacc')
]

fp = Player.make_player(user_input.output, pattern_makers)
cp = Player.make_player(output.ConsoleOutput(), pattern_makers)

