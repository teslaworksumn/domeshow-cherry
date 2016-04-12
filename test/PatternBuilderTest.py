import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src.pattern.PatternBuilder as PB

def test_build3():
    colorsA = [0, 0, 0, 10, 10, 10, 1, 1, 1, 11, 11, 11, 2, 2, 2, 12, 12, 12, 3, 3, 3, 13, 13, 13, 4, 4, 4, 14, 14, 14, 5, 5, 5, 15, 15, 15, 6, 6, 6, 16, 16, 16, 7, 7, 7, 17, 17, 17, 8, 8, 8, 18, 18, 18, 9, 9, 9, 19, 19, 19]
    colorsB = [20, 20, 20, 21, 21, 21, 30, 30, 30, 22, 22, 22, 23, 23, 23, 31, 31, 31, 24, 24, 24, 25, 25, 25, 32, 32, 32, 26, 26, 26, 27, 27, 27, 33, 33, 33, 28, 28, 28, 29, 29, 29, 34, 34, 34]
    colorsC = [35, 35, 35, 36, 36, 36, 37, 37, 37, 38, 38, 38, 39, 39, 39]

    expected = [i for eyes in [[n, n, n] for n in range(40)] for i in eyes]
    result = PB.build3([colorsA, colorsB, colorsC])

    assert(expected == result)


test_build3()
