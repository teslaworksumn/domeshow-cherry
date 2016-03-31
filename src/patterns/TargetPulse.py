import random
from src.patterns.Pattern import Pattern


# Pulse layer by layer, up or down
class TargetPulse(Pattern):
    def __init__(self, reversed):
        super().__init__()
        self.reversed = reversed
        self.color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.color2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        self.states = [
            self._patbuilder.build_data(self.color1, self.color1, self.color1, self.color1, self.color1),
            self._patbuilder.build_data(self.color2, self.color1, self.color1, self.color1, self.color1),
            self._patbuilder.build_data(self.color2, self.color2, self.color1, self.color1, self.color1),
            self._patbuilder.build_data(self.color2, self.color2, self.color2, self.color1, self.color1),
            self._patbuilder.build_data(self.color2, self.color2, self.color2, self.color2, self.color1),
            self._patbuilder.build_data(self.color2, self.color2, self.color2, self.color2, self.color2),
            self._patbuilder.build_data(self.color1, self.color2, self.color2, self.color2, self.color2),
            self._patbuilder.build_data(self.color1, self.color1, self.color2, self.color2, self.color2),
            self._patbuilder.build_data(self.color1, self.color1, self.color1, self.color2, self.color2),
            self._patbuilder.build_data(self.color1, self.color1, self.color1, self.color1, self.color2)
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


