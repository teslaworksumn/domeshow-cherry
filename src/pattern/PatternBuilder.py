

class PatternBuilder:
    def __init__(self):
        pass

    # Construct the data array from the patterns for each layer (repeated)
    # Layers are lists, multiples of 3, that contain channel rgb info
    def build_data(self, layer0, layer1, layer2, layer3, layer4):
        data = self._build_layer(layer0, False) + \
               self._build_layer(layer1, False) + \
               self._build_layer(layer2, False) + \
               self._build_layer(layer3, True) + \
               self._build_layer(layer4, True)
        return data

    # Helper function to create a layer's data output
    # small is whether this is layer 3 or 4, which only contain 5 panels
    # layer is a list of rgb values; must be multiple of 3
    def _build_layer(self, layer, small):
        if len(layer) % 3 != 0:
            raise ValueError(\
                'Expected layer length divisible by 3, was ' + str(len(layer)))

        colors = len(layer) // 3 # rgb colors in layer
        data = []
        triangle_count = 5 if small else 10

        for i in range(triangle_count):
            index = (i % colors) * 3
            data += layer[index:index + 3]

            # Skip every other triangle on small layers
            if small: data += [0, 0, 0]

        return data

        # Not sure this logic is right?
        # if small:
        #     Not sure this logic is right?
        #     for i in range(0, 5, len(layer) // 3):
        #         data += layer + [0, 0, 0]
        # else:
        #     for i in range(0, 10, len(layer) // 3):
        #         data += layer
        # return data[:30]