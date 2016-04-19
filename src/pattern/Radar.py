import src.pattern.PatternBuilder as PB
import random
from rx import Observable

last = [-1, -1, -1]

# Pulse layer by layer, up or down
def get_observable(
        color=None,
        reverse=None, # boolean
        tall=None, # boolean
        tick_period_ms=0):

    if color is None: color = PB.random_color()
    if reverse is None: reverse = (random.randint(0, 1) == 1)
    if tall is None: tall = (random.randint(0, 1) == 1)
    if tick_period_ms <= 0: tick_period_ms = 200

    if tall:
        builder = PB.build5
        count = 5
    else:
        builder = PB.build3
        count = 3

    layer_sets = [[last] * count for i in range(count)]
    for i in range(count):
        layer_sets[i][i] = color
    frames = [builder(layers) for layers in layer_sets]

    if reverse:
        access = lambda i: frames[-1 - i]
    else:
        access = lambda i: frames[i]

    return Observable.interval(tick_period_ms) \
        .take(len(frames)) \
        .map(access)
