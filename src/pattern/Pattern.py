from src.pattern.PatternBuilder import PatternBuilder

class Pattern:
    def __init__(self):
        self._patbuilder = PatternBuilder()

    def getframe(self, frame):
        NotImplementedError("getframe must be implemented in every Pattern")