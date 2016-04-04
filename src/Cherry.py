import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import rx
import src.Player as Player
import src.Output as output
from src.UserInput import UserInput
import atexit

user_input = UserInput()

pattern_makers = [
    lambda: ('Test pmaker', rx.Observable.repeat(list(range(10))).take(10))
]

player = Player.make_player(user_input.output, pattern_makers)

