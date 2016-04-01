import random
import rx.subjects.subject as rxsubject
from rx import Observable
from src.Output import FileOutput

from src.pattern.TargetPulse import TargetPulse
from src.pattern.FullRandom import FullRandom


# This class holds all of the dome's patterns and runs them
class Player:

    def __init__(self, device, numch, tick_period_ms, frames_per_pattern=32):
        self._num_channels = numch
        self._frames_per_pattern = frames_per_pattern
        self._tick_period_ms = tick_period_ms
        self._output = FileOutput(device)
        self._islooping = False
        self._stopstream = rxsubject.Subject()
        self.patterns = [FullRandom(numch),
                         TargetPulse(True),
                         TargetPulse(False),
                         self._rotatable_horizontal_wave, self._rotatable_horizontal_wave_continuous,
                         self._beach_ball_of_death, self._counter_rotating_circles, self._solid_fade,
                         self._full_random_fade, self._spiral, self._sets_of_5]

    # Starts running patterns
    def start(self):
        self._islooping = True
        self._next()

    # Stops all observables
    def shutdown(self):
        self._islooping = False
        self._stopstream.on_next(None)

    # Make the dome a solid color
    # Because the boards persistently hold their color, only send one set of data out
    def solid(self, r, g, b):
        self.shutdown()
        data = [r, g, b] * self._num_channels
        self._output.send(data)

    # Get the next pattern to play, and start it
    def _next(self):
        if self._islooping:
            self._stopstream.on_next(None)

            # TODO switch back (testing)
            # index = random.randint(0, len(self.patterns)-1)
            index = 0

            Observable.interval(self._tick_period_ms)\
                .take_until(self._stopstream)\
                .take(self._frames_per_pattern)\
                .map(lambda a,b: self.patterns[index].getframe(a))\
                .subscribe(self._output.send, lambda e: print(e), lambda: self._next())

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
