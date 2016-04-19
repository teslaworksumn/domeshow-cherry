import src.pattern.PatternBuilder as PB
from rx import Observable
import random

def _safe_colors(colors):
    if colors is None or len(colors) < 15:
        return [c for i in range(5) for c in PB.random_color()]
    return colors

def get_observable(colorsA=None, colorsB=None, tall=None, tick_period_ms=0):
    colors = [_safe_colors(colorsA), _safe_colors(colorsB)]
    if tall is None: tall = (random.randint(0, 1) == 1)
    if tick_period_ms <= 0: tick_period_ms = 200

    frames = [None] * 10
    
    for i in range(10):
        # Mutated, so shift 1 and -1 from last shift (cumulative shift)
        shifted = [PB.shift(colors[0], 0, 5, 1), PB.shift(colors[1], 0, 5, 4)]
        if tall:
            colors = [shifted[i % 2] for i in range(5)]
            frames[i] = PB.build5(colors)
        else:
            colors = [shifted[i % 2] for i in range(3)]
            frames[i] = PB.build3(colors)

    return Observable.interval(tick_period_ms) \
        .take(len(frames)) \
        .map(lambda i: frames[i])
