from src.pattern.Pattern import Pattern
import random


class FullRandom(Pattern):

    def __init__(self, numch):
        super().__init__()
        self._numchannels = numch

    def initialize(self):
        pass

    def getframe(self, frame):
        data = []
        for ch in range(self._numchannels):
            data += [random.randint(0, 255)]
        return data

