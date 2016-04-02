import random
from src.pattern.Pattern import Pattern


# Pulse layer by layer, up or down
class TargetPulse(Pattern):
    def __init__(self, reversed):
        super().__init__()
        self.reversed = reversed
        self.states = []
        self.initialize()

    def initialize(self):
        color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        color2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        self.states = [
            self._patbuilder.build_data(color1, color1, color1, color1, color1),
            self._patbuilder.build_data(color2, color1, color1, color1, color1),
            self._patbuilder.build_data(color2, color2, color1, color1, color1),
            self._patbuilder.build_data(color2, color2, color2, color1, color1),
            self._patbuilder.build_data(color2, color2, color2, color2, color1),
            self._patbuilder.build_data(color2, color2, color2, color2, color2),
            self._patbuilder.build_data(color1, color2, color2, color2, color2),
            self._patbuilder.build_data(color1, color1, color2, color2, color2),
            self._patbuilder.build_data(color1, color1, color1, color2, color2),
            self._patbuilder.build_data(color1, color1, color1, color1, color2),
            self._patbuilder.build_data(color1, color1, color1, color1, color1)
        ]


    def getframe(self, frame):
        numstates = len(self.states)
        if self.reversed:
            # 0 3 2 1 0 3 2 1 0 ... if numstates == 4
            index = numstates - ((numstates + frame - 1) % numstates) - 1
        else:
            # 0 1 2 3 0 1 2 3 0 ... if numstates == 4
            index = frame % numstates
        return self.states[index]


