import random
import rx.subjects.subject as rxsubject
from rx import Observable
from src.Output import FileOutput

from src.pattern.TargetPulse import TargetPulse
from src.pattern.FullRandom import FullRandom

## General idea
# 
# make pattern stream:
# 1. Observable.repeat(None)
# 2. map(getRandomIndex)
# 3. map(lambda i: patterns[i])
# 4. concat_all()
#
# state stream: will be a stream of PlayerState
# enum PlayerState {
#   Patterns,
#   Solid(i8 r, i8 g, i8 b),
# }
#
# data stream:
# 1. state_stream
# 2. map(state -> match (state) {
#        Solid(r, g, b) = Observable.never().start_with([r, g, b] * 40),
#        Pattern = make_pattern_stream(),
#    })
# 3. switch()


# This class holds all of the dome's patterns and runs them
class Player:

    def __init__(self, device, num_channels):
        self._num_channels = num_channels
        self._output = FileOutput(device)
        self._state_stream = rxsubject.Subject()
        self.patterns = []

        self._data_stream

    def run_patterns

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
