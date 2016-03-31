import src.patterns.PatternBuilder as PatternBuilder

class Pattern:
    def __init__(self):
        self._patbuilder = PatternBuilder.PatternBuilder()

    def getframe(self, frame):
        NotImplementedError("getframe must be implemented in every Pattern")