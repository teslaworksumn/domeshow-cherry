

class Output:
    def __init__(self, device):
        self.device = device

    # Data is a dictionary of length 120 (40 lights * 3 channels)
    # where each element is the 8-bit value for that channel
    def send(self, data):
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
        data = []
        if len(layer) % 3 != 0:
            print('Layer has to have length that is multiple of 3 (rgb)')
            return None
        if small:
            for i in range(0, 5, len(layer) // 3):
                data += layer + [0, 0, 0]
        else:
            for i in range(0, 10, len(layer) // 3):
                data += layer
        return data[:30]
