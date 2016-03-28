import random
import rx.subjects
import rx.linq.observable.interval as rxinterval


# This class holds all of the dome's patterns and runs them
class Patterns:

    # tickrate is in ms
    def __init__(self, numchannels, tickrate):
        self._numchannels = numchannels
        self._tickrate = tickrate

    def start(self):
        self._next()

    def solid(self, color):
        data = [color] * self._numchannels

    def _next(self):
        patterns = [self._full_random, self._target, self._reverse_target,
                    self._rotatable_horizontal_wave, self._rotatable_horizontal_wave_continuous,
                    self._beach_ball_of_death, self._counter_rotating_circles, self._solid_fade,
                    self._full_random_fade, self._spiral, self._sets_of_5]
        index = random.randint(0, len(patterns)-1)


    def _error(self, err):
        print("Error:", err)

    def _exit(self):
        print("Exiting...")

    def _full_random(self):
        print('full random')

    def _target(self):
        print('target')

    def _reverse_target(self):
        print('reverse target')

    def _rotatable_horizontal_wave(self):
        print('rotatable horizontal wave')

    def _rotatable_horizontal_wave_continuous(self):
        print('rotatable horizontal wave continuous')

    def _beach_ball_of_death(self):
        print('beach ball of death')

    def _counter_rotating_circles(self):
        print('counter rotating circles')

    def _solid_fade(self):
        print('solid fade')

    def _full_random_fade(self):
        print('full random fade')

    def _spiral(self):
        print('spiral')

    def _sets_of_5(self):
        print('sets of 5')

