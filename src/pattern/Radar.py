import src.pattern.PatternBuilder as PB
import random
from rx import Observable

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

    last = [-1, -1, -1]

    if tall:
        layer_sets = [(i * [last]) + [color] + ((4-i) * [last]) for i in range(5)]
        frames = [PB.build5(layers) for layers in layer_sets]
    else:
        layer_sets = [(i * [last]) + [color] + ((2-i) * [last]) for i in range(3)]
        frames = [PB.build3(layers) for layers in layer_sets]

    if reverse:
        frames = frames[::-1]

    return Observable.from_list(frames) \
        .map(lambda frame: (frame, tick_period_ms))
