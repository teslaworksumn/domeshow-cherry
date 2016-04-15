import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src.Player as Player
from src.output.FileOutput import FileOutput as FileOutput
from src.output.ConsoleOutput import ConsoleOutput as ConsoleOutput
from src.output.SerialOutput import SerialOutput as SerialOutput
import src.pattern.FullRandom as full_random
import src.pattern.Tsunami as tsunami
import src.pattern.Sarlacc as sarlacc
import src.pattern.Radar as radar
import src.pattern.CounterRotatingCircles as crc
from src.UserInput import UserInput

user_input = UserInput()

pattern_makers = [
    lambda: (full_random.get_observable(), 'Full Random'),
    lambda: (tsunami.get_observable(), 'Tsunami'),
    lambda: (sarlacc.get_observable(), 'Sarlacc'),
    lambda: (radar.get_observable(), 'Radar'),
    lambda: (crc.get_observable(), 'Counter Rotating Circles')
]

fp = Player.make_player(FileOutput(user_input.output), pattern_makers)
cp = Player.make_player(ConsoleOutput(), pattern_makers)
sp = Player.make_player(SerialOutput(user_input.output), pattern_makers)
