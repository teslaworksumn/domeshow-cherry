import random
import rx.subjects.subject as rxsubject
from rx import Observable
from rx.concurrency import scheduler
import src.Output as Output


# This class holds all of the dome's patterns and runs them
class Patterns:

    # tickrate is in ms
    def __init__(self, device, numchannels, tickrate):
        self._numchannels = numchannels
        self._tickrate = tickrate
        self._output = Output.Output(device)
        self._stopstream = rxsubject.Subject()

    # Starts running patterns
    def start(self):
        self._next()

    # Stops all observables
    def shutdown(self):
        self._stopstream.on_next(None)

    # Make the dome a solid color
    def solid(self, r, g, b):
        self._stopstream.on_next(None)
        data = [r, g, b] * self._numchannels
        self._output.send(data)

    # Get the next pattern to play, and start it
    def _next(self):
        self._stopstream.on_next(None)
        patterns = [self._full_random, self._target, self._reverse_target,
                    self._rotatable_horizontal_wave, self._rotatable_horizontal_wave_continuous,
                    self._beach_ball_of_death, self._counter_rotating_circles, self._solid_fade,
                    self._full_random_fade, self._spiral, self._sets_of_5]
        index = random.randint(0, len(patterns)-1)
        index = 1
        self._tickstream = Observable.interval(self._tickrate)\
            .take_until(self._stopstream)\
            .map(lambda a,b: patterns[index](a))\
            .subscribe(self._output.send)

    # Each triangle is a random color
    # Changes each tick for 4 ticks
    def _full_random(self, frame):
        if frame < 4:
            data = []
            for ch in range(self._numchannels):
                data += [random.randint(0, 255)]
            return data
        else:
            self._next()
            return None

    def _target(self, frame):
        color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        color2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        color1 = [1, 1, 1]
        color2 = [2, 2, 2]
        data = self._output.build_data(color1, color1, color2, color2, color1)
        print(data)
        return data
#
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#  1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
#

    def _reverse_target(self, frame):
        pass

    def _rotatable_horizontal_wave(self, frame):
        pass

    def _rotatable_horizontal_wave_continuous(self, frame):
        pass

    def _beach_ball_of_death(self, frame):
        pass

    def _counter_rotating_circles(self, frame):
        pass

    def _solid_fade(self, frame):
        pass

    def _full_random_fade(self, frame):
        pass

    def _spiral(self, frame):
        pass

    def _sets_of_5(self, frame):
        pass