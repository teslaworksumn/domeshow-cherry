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
import src.pattern.BeachBall as beach_ball
import src.pattern.Pulse as pulse
import src.pattern.Spiral as spiral
from src.UserInput import UserInput

user_input = UserInput()

pattern_makers = [
    lambda: (full_random.get_observable(), 'Full Random'),
    lambda: (tsunami.get_observable(), 'Tsunami'),
    lambda: (sarlacc.get_observable(), 'Sarlacc'),
    lambda: (radar.get_observable(), 'Radar'),
    lambda: (crc.get_observable(), 'Counter Rotating Circles'),
    lambda: (beach_ball.get_observable(), 'Beach Ball'),
    lambda: (pulse.get_observable(), 'Pulse'),
    lambda: (spiral.get_observable(), 'Spiral')
]

cp = Player.make_player(ConsoleOutput(), pattern_makers)
try:
    fp = Player.make_player(FileOutput(user_input.output), pattern_makers)
except Exception:
    print('Failed to open FileOutput with output "', user_input.output, '"', sep='')

try:
    sp = Player.make_player(SerialOutput(user_input.output), pattern_makers)
except Exception:
    print('Failed to open SerialOutput with output "', user_input.output, '"', sep='')

