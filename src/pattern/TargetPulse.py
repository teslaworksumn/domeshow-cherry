import src.pattern.PatternBuilder as PB
import random
from rx import Observable

# Pulse layer by layer, up or down
def get_observable(
        color1=None,
        color2=None,
        reverse=False,
        tick_period_ms=0,
        num_frames=-1):

    if color1 is None: color1 = PB.random_color()
    if color2 is None: color2 = PB.random_color()
    if tick_period_ms <= 0: tick_period_ms = 200
    if num_frames < 0: num_frames = random.randint(3, 6) * 11

    layer_buffer = ([color1] * 5) + ([color2] * 5) + ([color1] * 5)

    states = [
        PB.build_data(*(layer_buffer[i:i+5])) for i in range(11)
    ]

    increment = -1 if reverse else 1

    # Observable
    return Observable.interval(tick_period_ms) \
        .scan(0, lambda acc, x: (acc + increment) % num_frames) \
        .take(num_frames) \
        .map(lambda i: states[i])
