import src.pattern.PatternBuilder as PB
import random
from rx import Observable

last = [-1, -1, -1]

def get_observable(color=None, offset=0, tick_period_ms=0):
    if color is None: color = PB.random_color()
    if tick_period_ms <= 0: tick_period_ms = 200

    layer_sets = [[last] * 10 for i in range(10)]

    for i in range(10):
        layer_sets[i][i] = color

    unordered_frames = [PB.build10(layers, offset) for layers in layer_sets]

    frames = \
        [unordered_frames[i] for i in range(0, 9, 2)] + \
        [unordered_frames[i] for i in range(9, 0, -2)]

    return Observable.interval(tick_period_ms) \
        .take(len(frames)) \
        .map(lambda i: frames[i])
