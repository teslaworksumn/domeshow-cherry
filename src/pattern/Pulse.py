import src.pattern.PatternBuilder as PB
import random
from rx import Observable

def get_observable(on_color=None, tick_period_ms=0):
    if on_color is None: on_color = PB.random_color()
    if tick_period_ms <= 0: tick_period_ms = 150

    colors = [
        [0, 0, 0],
        [c // 4 for c in on_color],
        [c // 2 for c in on_color],
        [(c * 3) // 4 for c in on_color],
        on_color
    ]
    colors += colors[3:0:-1] # dim back down

    frames = [color * 40 for color in colors] * 4

    return Observable.interval(tick_period_ms) \
        .take(len(frames)) \
        .map(lambda i: frames[i])
