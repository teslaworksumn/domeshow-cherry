import random
import rx.subjects.subject as rxsubject
from rx import Observable
import src.Output as Output

from src.patterns.TargetPulse import TargetPulse
from src.patterns.FullRandom import FullRandom


# This class holds all of the dome's patterns and runs them
class Patterns:

    # tickrate is in ms
    def __init__(self, device, numch, tickrate):
        self._numchannels = numch
        self._tickrate = tickrate
        self._output = Output(device)
        self._stopstream = rxsubject.Subject()
        self.patterns = [FullRandom(numch), TargetPulse(True), TargetPulse(False),
                         self._rotatable_horizontal_wave, self._rotatable_horizontal_wave_continuous,
                         self._beach_ball_of_death, self._counter_rotating_circles, self._solid_fade,
                         self._full_random_fade, self._spiral, self._sets_of_5]

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
        index = random.randint(0, len(self.patterns)-1)
        # TODO remove (testing)
        index = 0
        self._tickstream = Observable.interval(self._tickrate)\
            .take_until(self._stopstream)\
            .map(lambda a,b: self.patterns[index].getframe(a))\
            .subscribe(self._output.send)

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
