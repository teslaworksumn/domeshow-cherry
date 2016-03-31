#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import src.Output as Output

def build_layer_works_nosmall():
    o = Output('/dev/null')
    l = o._build_layer([1, 2, 3], False)
    print(l == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

def build_layer_works_small():
    pass


build_layer_works_nosmall()
build_layer_works_small()
