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
    data = [0] * 40

    _build_layer(data, 0, layers[0], 10)
    _build_layer(data, 30, layers[1], 10)
    _build_layer(data, 60, layers[2], 10)
    _build_layer(data, 90, layers[3], 5)
    _build_layer(data, 105, layers[4], 5)

    return data

def build3(layers):
    # bottom is the simple alternation between layer0 and layer1
    # middle follows the pattern layer2 layer2 layer3
    # This is because there are 10 layer2 triangles, but only 5 layer3 triangles
    # top is simply layer4

    buf = [0] * 120
    data = [0] * 120

    _build_layer(buf, 0, layers[0], 20)
    _build_layer(buf, 60, layers[1], 15)
    _build_layer(data, 105, layers[2], 5)

    for i in range(3): # layer 0
        data[i:30:3] = data[i:60:6]
    for i in range(3): # layer 1
        data[i+30:60:3] = data[i+3:60:6]
    for i in range(6): # layer 2
        data[i+60:90:6] = data[i+60:105:9]
    for i in range(3): # layer 3
        data[i+90:105:3] = data[i+66:105:9]

    return data


def build10(layers, offset):
    return \
        shift(offset, _build_layer(layers[0], 5) + _build_layer(layers[1], 5)) + \
        shift(offset, _build_layer(layers[2], 5) + _build_layer(layers[3], 5)) + \
        shift(offset, _build_layer(layers[4], 5) + _build_layer(layers[5], 5)) + \
        shift(offset, _build_layer(layers[6], 3) + _build_layer(layers[7], 2)) + \
        shift(offset, _build_layer(layers[8], 3) + _build_layer(layers[9], 2))

# Shifts the colors in a layer left by a number of spots
def shift(offset, layer):
    offset = (offset * 3) % len(layer)
    return layer[offset:] + layer[:offset]

# Helper function to create a layer's data output
# data is the array to modify and offset is how far to start writing
# layer is a list of rgb values; must be multiple of 3
# triangle_count is the number of panels/triangles in this layer
def _build_layer(data, offset, layer, triangle_count):
    if len(layer) % 3 != 0:
        raise ValueError( \
            'Expected layer length divisible by 3, was ' + str(len(layer)))

    colors = len(layer) // 3  # rgb colors in layer

    for i in range(triangle_count):
        l_index = (i % colors) * 3
        d_index = offset + (i * 3)
        data[d_index:d_index + 3] = layer[l_index:l_index + 3]


