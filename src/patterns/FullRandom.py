import src.pattern.PatternBuilder as PatternBuilder
import random
from rx import Observable


def get_frame(frame):
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return PatternBuilder.build_data(color, color, color, color, color)


def get_observable(tick_period_ms=0, num_frames=-1):
    # Parameters
    if tick_period_ms <= 0: tick_period_ms = random.randint(1000, 3000)
    if num_frames < 0: num_frames = random.randint(4, 6)

    # Observable
    return Observable.interval(tick_period_ms) \
        .take(num_frames) \
        .map(lambda a, b: get_frame(a))


