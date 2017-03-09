import sys
import os

import Player as Player
from output.FileOutput import FileOutput as FileOutput
from output.ConsoleOutput import ConsoleOutput as ConsoleOutput
from output.SerialOutput import SerialOutput as SerialOutput
import pattern.FullRandom as full_random
import pattern.Tsunami as tsunami
import pattern.Sarlacc as sarlacc
import pattern.Radar as radar
import pattern.CounterRotatingCircles as crc
import pattern.BeachBall as beach_ball
import pattern.Pulse as pulse
import pattern.Spiral as spiral
from UserInput import UserInput

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

