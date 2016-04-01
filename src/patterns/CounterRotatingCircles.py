from src.patterns.Pattern import Pattern
import random


class CounterRotatingCircles(Pattern):

    # numcolors is number of distinct colors in a layer
    def __init__(self, numcolors):
        super().__init__()
        self.states = []
        self._numcolors = numcolors
        self.initialize()

    def initialize(self):
        colorsA = []
        colorsB = []
        for i in range(self._numcolors):
            colorsA += [i, i, i]#[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            colorsB += [i+2, i+2, i+2]#[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        # Double size of color lists to allow for simple modulo slicing
        self.colorsA = colorsA + colorsA
        self.colorsB = colorsB + colorsB

    def getframe(self, frame):
        indexA = frame % self._numcolors
        indexB = (self._numcolors - frame - 1) % self._numcolors
        layerA = self.colorsA[3*indexA:3*(indexA+self._numcolors)]
        layerB = self.colorsB[3*indexB:3*(indexB+self._numcolors)]
        return self._patbuilder.build_data(layerA, layerB, layerA, layerB, layerA)
