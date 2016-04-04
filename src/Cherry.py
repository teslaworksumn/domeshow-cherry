#!/usr/bin/env python3 -i

import sys
import os
import rx
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src.Player
from src.Output import FileOutput
from src.UserInput import UserInput
import atexit

output = FileOutput('/tmp/cherrylog')

pattern_makers = [
    lambda: ('Test pmaker', rx.Observable.repeat(list(range(144))).take(10))
]

player = Player.make_player(output, pattern_makers)

