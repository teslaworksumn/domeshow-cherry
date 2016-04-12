import random

# Generates a random color as [r, g, b]
def random_color():
    return [
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    ]

# Construct the data array from the patterns for each layer (repeated)
# Layers are lists, multiples of 3, that contain channel rgb info
def build5(layers):
    data = \
        _build_layer(layers[0], 10) + \
        _build_layer(layers[1], 10) + \
        _build_layer(layers[2], 10) + \
        _build_layer(layers[3], 5) + \
        _build_layer(layers[4], 5)
    return data

def build3(layers):
    # bottom is the simple alternation between layer0 and layer1
    # middle follows the pattern layer2 layer2 layer3
    # This is because there are 10 layer2 triangles, but only 5 layer3 triangles
    # top is simply layer4
    bottom = _build_layer(layers[0], 20)
    middle = _build_layer(layers[1], 15)
    top = _build_layer(layers[2], 5)

    layer0 = [0] * 30
    layer1 = [0] * 30
    layer2 = [0] * 30
    layer3 = [0] * 15
    layer4 = top

    for i in range(6):
        layer2[i::6] = middle[i::9]
    for i in range(3):
        layer0[i::3] = bottom[i::6]
        layer1[i::3] = bottom[i + 3::6]
        layer3[i::3] = middle[i + 6::9]

    return layer0 + layer1 + layer2 + layer3 + layer4


def build10(layers, offset):
    return \
        _shift(offset, _build_layer(layers[0], 5) + _build_layer(layers[1], 5)) + \
        _shift(offset, _build_layer(layers[2], 5) + _build_layer(layers[3], 5)) + \
        _shift(offset, _build_layer(layers[4], 5) + _build_layer(layers[5], 5)) + \
        _shift(offset, _build_layer(layers[6], 3) + _build_layer(layers[7], 2)) + \
        _shift(offset, _build_layer(layers[8], 3) + _build_layer(layers[9], 2))

# Shifts the colors in a layer left by a number of spots
def _shift(offset, layer):
    offset = (offset * 3) % len(layer)
    return layer[offset:] + layer[:offset]

# Helper function to create a layer's data output
# layer is a list of rgb values; must be multiple of 3
# triangle_count is the number of panels/triangles in this layer
def _build_layer(layer, triangle_count):
    if len(layer) % 3 != 0:
        raise ValueError( \
            'Expected layer length divisible by 3, was ' + str(len(layer)))

    colors = len(layer) // 3  # rgb colors in layer
    data = []

    for i in range(triangle_count):
        index = (i % colors) * 3
        data += layer[index:index + 3]

    return data


