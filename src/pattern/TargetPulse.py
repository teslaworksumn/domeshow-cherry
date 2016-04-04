import src.pattern.PatternBuilder as PatternBuilder
import random
from rx import Observable


# Pulse layer by layer, up or down
def get_observable(reverse=False, color1=None, color2=None, tick_period_ms=0, num_frames=-1):
    # Parameters
    if color1 is None: color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if color2 is None: color2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    states = [
        PatternBuilder.build_data(color1, color1, color1, color1, color1),
        PatternBuilder.build_data(color2, color1, color1, color1, color1),
        PatternBuilder.build_data(color2, color2, color1, color1, color1),
        PatternBuilder.build_data(color2, color2, color2, color1, color1),
        PatternBuilder.build_data(color2, color2, color2, color2, color1),
        PatternBuilder.build_data(color2, color2, color2, color2, color2),
        PatternBuilder.build_data(color1, color2, color2, color2, color2),
        PatternBuilder.build_data(color1, color1, color2, color2, color2),
        PatternBuilder.build_data(color1, color1, color1, color2, color2),
        PatternBuilder.build_data(color1, color1, color1, color1, color2),
    ]

    if tick_period_ms <= 0: tick_period_ms = random.randint(200, 1000)
    if num_frames < 0: num_frames = random.randint(3, 6) * len(states)

    increment = -1 if reverse else 1

    # Observable
    return Observable.interval(tick_period_ms) \
        .scan(0, lambda acc, x: (acc + increment) % num_frames) \
        .take(num_frames) \
        .map(lambda i: states[i])


