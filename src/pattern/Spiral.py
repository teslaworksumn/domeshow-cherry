import src.pattern.PatternBuilder as PB
import random
from rx import Observable

def get_observable(color=None, tick_period_ms=0):
    if color is None: color = PB.random_color()
    if tick_period_ms <= 0: tick_period_ms = 50

    frames = [[-1] * 120 for i in range(40)]

    for i in range(40):
        frames[i][i*3:(i+1)*3] = color

    return Observable.interval(tick_period_ms) \
        .take(len(frames)) \
        .map(lambda i: frames[i])
